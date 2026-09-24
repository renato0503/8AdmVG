"""Monta _pesquisa/selecionados/G<n>.json apenas com registros que EXISTEM nos brutos da API
(_pesquisa/saidas/G<n>_*.json). Se um DOI da lista nao estiver nos brutos, o script falha.
Isso garante que nenhuma referencia usada nos Pesquisa-Dados.md foi inventada."""
import glob, json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
SELECAO = {
 "G1": ["10.5747/cs.2024.v8.s178","10.66104/zh5a8c55","10.22421/1517-7130/es.2025v26.e1090",
        "10.1080/0309877x.2021.1951687","10.1080/21568235.2023.2202874","10.1080/13639080.2023.2167955",
        "10.1108/cdi-02-2020-0036","10.1016/j.heliyon.2024.e27332","10.1080/07294360.2021.1902951",
        "10.18608/jla.2023.7935","10.14786/flr.v11i2.1277","10.1111/jcal.12853",
        "10.3390/computers10100132","10.1007/s11423-026-10586-2"],
 "G2": ["10.21325/jotags.2024.1388","10.3390/digital4010014","10.1371/journal.pone.0294244",
        "10.1080/17538947.2022.2130456","10.1016/j.iswa.2023.200263","10.3390/su14053048",
        "10.3390/su14052721","10.3390/su13021007","10.1080/1331677x.2020.1867215",
        "10.1177/13567667231152938","10.1080/13683500.2022.2126965",
        "10.1080/13683500.2022.2048804","10.31637/epsir-2026-1979","10.1080/02508281.2025.2598874"],
 "G3": ["10.1016/j.heliyon.2024.e31825","10.1016/j.eswa.2022.118720","10.1109/access.2021.3111544",
        "10.3390/app12062802","10.3389/fresc.2024.1368983","10.3390/s23010367",
        "10.1177/23998083241256402","10.3389/fmed.2024.1361631","10.3389/fpsyg.2021.731693",
        "10.3390/disabilities3040040","10.1098/rsta.2024.0106",
        "10.3895/rts.v17n47.11549","10.9771/cp.v15i1.43946","10.3390/app12010523"],
 "G4": ["10.1108/sasbe-03-2021-0056","10.1016/j.dss.2023.114131","10.1287/isre.2021.9138",
        "10.1080/02673037.2022.2074971","10.1016/j.chb.2023.107996","10.1017/flw.2023.3",
        "10.1016/j.jbankfin.2024.107170","10.1016/j.jbef.2025.101077","10.1093/rfs/hhaa096",
        "10.1108/el-09-2024-0261","10.1108/ijhma-07-2022-0095","10.6007/ijarbss/v11-i7/10295",
        "10.1016/j.jfineco.2026.104239","10.3390/electronics12030707"],
 "G5": ["10.1111/blar.13261","10.1590/1678-6971/eramg210115","10.1590/1678-98732230e020",
        "10.21527/2237-6453.2021.55.10215","10.1016/j.landusepol.2026.108081",
        "10.1590/0034-761220190341","10.5334/bc.180",
        "10.1590/2236-9996.2026-6571161-en","10.1093/ppmgov/gvab027","10.1016/j.giq.2021.101653",
        "10.1093/ppmgov/gvac024","10.7758/rsf.2023.9.5.05","10.3390/su17072908","10.1111/padm.70059"],
}
def main(dump=False):
    ok = True
    for g, dois in SELECAO.items():
        brutos = {}
        for f in sorted(glob.glob(f"saidas/{g}_*.json")):
            for it in json.load(open(f, encoding="utf-8")):
                if it["doi"]:
                    brutos.setdefault(it["doi"].lower(), dict(it, arquivo_bruto=f.replace("\\", "/")))
        sel = []
        for d in dois:
            r = brutos.get(d.lower())
            if not r:
                print(f"FALHA {g}: {d} nao existe nos brutos"); ok = False; continue
            sel.append(r)
        json.dump(sel, open(f"selecionados/{g}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{g}: {len(sel)}/{len(dois)} confirmados nos brutos")
        if dump:
            for i, r in enumerate(sel, 1):
                print(f"\n[{g}.{i}] {r['autores']} ({r['ano']}). {r['titulo']}. {r['periodico']}. DOI {r['doi']} | cit {r['citacoes']} | OA {r['acesso_aberto']}\n   {r['abstract'][:650]}")
    sys.exit(0 if ok else 1)
if __name__ == "__main__":
    main("--dump" in sys.argv)
