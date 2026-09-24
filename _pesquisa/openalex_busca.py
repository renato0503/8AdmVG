"""Busca artigos peer-reviewed no OpenAlex (e confere DOI na Crossref).

Ferramenta de apoio a pesquisa dos 6 grupos do projeto 8AdmVG (Customer Discovery).
Usa apenas a biblioteca padrao do Python. Rodar com `py openalex_busca.py ...`.

Exemplos:
    py openalex_busca.py --tema "consumer behavior digital government services" --limit 20
    py openalex_busca.py --tema "telemedicine mental health help-seeking" --desde 2021 --ate 2026 --json saida.json
    py openalex_busca.py --doi 10.1016/j.jbusres.2021.01.001 --conferir-crossref

Regras: nunca inventar metadados. Tudo o que sai veio da API (OpenAlex ou Crossref).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MAILTO = "renato.rosa@unifacc.edu.br"
UA = f"8AdmVG-CustomerDiscovery/1.0 (mailto:{MAILTO})"
OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"


def _get(url: str, tentativas: int = 8) -> dict | None:
    import random
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for a in range(tentativas):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            espera = min(30, 3 * (a + 1)) + random.uniform(0, 3)
            time.sleep(espera)
        except Exception:
            time.sleep(min(30, 3 * (a + 1)))
    return None


def resumo_abstract(inv: dict | None, limite: int = 700) -> str:
    if not inv:
        return ""
    pos = {}
    for palavra, idxs in inv.items():
        for i in idxs:
            pos[i] = palavra
    txt = " ".join(pos[i] for i in sorted(pos))
    txt = " ".join(txt.split())
    return txt[:limite] + ("..." if len(txt) > limite else "")


def autores_txt(autores: list[dict], limite: int = 4) -> str:
    nomes = [a.get("author", {}).get("display_name", "") for a in autores or []]
    nomes = [n for n in nomes if n]
    if not nomes:
        return "s/ autor listado"
    if len(nomes) <= limite:
        return "; ".join(nomes)
    return "; ".join(nomes[:limite]) + " et al."


def fonte(work: dict) -> str:
    pl = work.get("primary_location") or {}
    src = pl.get("source") or {}
    return src.get("display_name") or (work.get("host_venue") or {}).get("display_name") or ""


def oa_url(work: dict) -> str:
    oa = work.get("open_access") or {}
    if oa.get("oa_url"):
        return oa["oa_url"]
    pl = work.get("primary_location") or {}
    return pl.get("landing_page_url") or ""


def normaliza(work: dict) -> dict:
    return {
        "titulo": work.get("title") or "",
        "ano": work.get("publication_year"),
        "autores": autores_txt(work.get("authorships", [])),
        "periodico": fonte(work),
        "tipo": work.get("type"),
        "doi": (work.get("doi") or "").replace("https://doi.org/", ""),
        "citacoes": work.get("cited_by_count"),
        "acesso_aberto": bool((work.get("open_access") or {}).get("is_oa")),
        "url": oa_url(work),
        "areas": [t.get("display_name") for t in (work.get("topics") or [])[:3]],
        "abstract": resumo_abstract(work.get("abstract_inverted_index")),
        "openalex_id": work.get("id"),
    }


CAMPOS = ("search", "title_and_abstract", "title")


def busca(termo: str, desde: int, ate: int, limite: int, campo: str = "title_and_abstract",
          citacoes_min: int = 0, somente_artigo: bool = True) -> list[dict]:
    if campo not in CAMPOS:
        campo = "title_and_abstract"
    filtros = [f"from_publication_date:{desde}-01-01", f"to_publication_date:{ate}-12-31"]
    if somente_artigo:
        filtros.append("type:article")
    chave = "search" if campo == "search" else f"{campo}.search"
    filtros.append(f"{chave}:{termo}")
    if citacoes_min:
        filtros.append(f"cited_by_count:>{citacoes_min - 1}")
    q = {
        "filter": ",".join(filtros),
        "sort": "relevance_score:desc",
        "per_page": str(min(limite, 50)),
        "mailto": MAILTO,
    }
    url = OPENALEX + "?" + urllib.parse.urlencode(q)
    dados = _get(url)
    if not dados:
        return []
    return [normaliza(w) for w in dados.get("results", []) if w.get("title")]


def conferir_crossref(doi: str) -> dict | None:
    url = CROSSREF + "/" + urllib.parse.quote(doi)
    dados = _get(url)
    if not dados:
        return None
    it = dados.get("message", {})
    return {
        "titulo": (it.get("title") or [""])[0],
        "ano": ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0],
        "periodico": (it.get("container-title") or [""])[0],
        "doi": it.get("DOI"),
        "tipo": it.get("type"),
    }


def imprime_md(itens: list[dict], termo: str, arquivo: str | None) -> None:
    linhas = [f"# Busca OpenAlex: {termo}", ""]
    for i, it in enumerate(itens, 1):
        linhas.append(f"## {i}. {it['titulo']}")
        linhas.append(f"- Autores: {it['autores']}")
        linhas.append(f"- Ano: {it['ano']} | Periodico: {it['periodico'] or 'n/d'} | Tipo: {it['tipo']}")
        linhas.append(f"- DOI: {it['doi'] or 'n/d'} | Citacoes: {it['citacoes']} | OA: {it['acesso_aberto']}")
        if it["areas"]:
            linhas.append(f"- Areas: {', '.join(a for a in it['areas'] if a)}")
        if it["url"]:
            linhas.append(f"- Link: {it['url']}")
        if it["abstract"]:
            linhas.append(f"- Resumo: {it['abstract']}")
        linhas.append("")
    texto = "\n".join(linhas)
    if arquivo:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"OK: {len(itens)} itens -> {arquivo}")
    else:
        print(texto)


def main() -> None:
    ap = argparse.ArgumentParser(description="Busca OpenAlex + conferencia Crossref")
    ap.add_argument("--tema", help="termo de busca (ingles costuma render mais)")
    ap.add_argument("--desde", type=int, default=2021)
    ap.add_argument("--ate", type=int, default=2026)
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--campo", choices=CAMPOS, default="title_and_abstract",
                    help="onde buscar o termo (padrao: title_and_abstract)")
    ap.add_argument("--citacoes-min", type=int, default=0, help="so artigos com pelo menos N citacoes")
    ap.add_argument("--json", dest="json_out", help="salva tambem um JSON")
    ap.add_argument("--md", help="salva tabela markdown em arquivo")
    ap.add_argument("--doi", help="so confere um DOI na Crossref")
    ap.add_argument("--conferir-crossref", action="store_true", help="confere os DOIs encontrados na Crossref")
    args = ap.parse_args()

    if args.doi:
        info = conferir_crossref(args.doi)
        print(json.dumps(info, ensure_ascii=False, indent=2) if info else "nao encontrado")
        return

    if not args.tema:
        print("informe --tema ou --doi", file=sys.stderr)
        sys.exit(2)

    itens = busca(args.tema, args.desde, args.ate, args.limit, args.campo, args.citacoes_min)
    if args.conferir_crossref:
        for it in itens:
            if it["doi"]:
                cr = conferir_crossref(it["doi"])
                if cr:
                    it["crossref_ano"] = cr["ano"]
                    it["crossref_doi_ok"] = bool(cr["doi"])
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(itens, f, ensure_ascii=False, indent=2)
        print(f"OK: {len(itens)} itens -> {args.json_out}")
    if args.md or not args.json_out:
        imprime_md(itens, args.tema, args.md)


if __name__ == "__main__":
    main()
