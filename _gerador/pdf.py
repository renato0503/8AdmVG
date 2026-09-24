"""Gera os PDFs do 8AdmVG (slides reveal.js + cadernos) com Playwright/Chromium.

Mais estável que o `chrome --print-to-pdf` usado no 3SemVG: espera a rede e o reveal.js
terminarem de montar as páginas antes de imprimir, então não sai PDF de 1 página em branco.

Uso (da raiz 8AdmVG):
    py _gerador/pdf.py                 # todos
    py _gerador/pdf.py Grupo3 "Parte 1"  # só os que contêm algum dos filtros no caminho
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent

SLIDES = sorted(RAIZ.glob("Grupo*/Slides-*.html")) + sorted(RAIZ.glob("Parte */Slides-*.html"))
CADERNOS = sorted(RAIZ.glob("Parte */caderno-*.html"))


def paginas(pdf: Path) -> int:
    import fitz
    return fitz.open(pdf).page_count


def main(filtros):
    jobs = [(p, True) for p in SLIDES] + [(p, False) for p in CADERNOS]
    if filtros:
        jobs = [j for j in jobs if any(f.lower() in str(j[0]).lower() for f in filtros)]
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        pg = nav.new_page()
        for html, slide in jobs:
            url = html.as_uri() + ("?print-pdf" if slide else "")
            pg.goto(url, wait_until="networkidle")
            if slide:
                pg.wait_for_function("window.Reveal && Reveal.isReady && Reveal.isReady()", timeout=30000)
                pg.wait_for_selector(".pdf-page", state="attached", timeout=30000)
            pg.wait_for_timeout(800)
            out = html.with_suffix(".pdf")
            if slide:
                pg.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
            else:
                pg.pdf(path=str(out), format="A4", print_background=True,
                       margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"})
            n = paginas(out)
            aviso = ""
            if slide:
                secoes = pg.evaluate("document.querySelectorAll('.slides section').length")
                if n != secoes:
                    aviso = f"  <-- {secoes} slides mas {n} páginas: algum slide transbordou"
            print(f"{out.relative_to(RAIZ)}: {n} pág.{aviso}")
        nav.close()


if __name__ == "__main__":
    main(sys.argv[1:])
