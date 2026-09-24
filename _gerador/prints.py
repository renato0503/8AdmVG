"""Capturas de tela das abas de um app (375x667) lado a lado — para revisão visual.
Uso: py _gerador/prints.py Grupo1  -> salva em %TEMP%/claude/prints_<grupo>.png"""
import sys, os, tempfile
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
RAIZ = Path(__file__).resolve().parent.parent
alvo = next(RAIZ.glob(f"{sys.argv[1]}*/app.html"))
saida = Path(tempfile.gettempdir()) / "claude"; saida.mkdir(exist_ok=True)
with sync_playwright() as pw:
    nav = pw.chromium.launch(); pg = nav.new_page(viewport={"width": 375, "height": 740}, device_scale_factor=1)
    pg.goto(alvo.as_uri()); pg.wait_for_timeout(500)
    abas = pg.eval_on_selector_all(".nav-inf [data-aba]", "els => els.map(e => e.dataset.aba)")
    ims = []
    for a in abas:
        pg.click(f'.nav-inf [data-aba="{a}"]'); pg.wait_for_timeout(300)
        f = saida / f"_p_{a}.png"; pg.screenshot(path=str(f)); ims.append(Image.open(f))
    nav.close()
W = Image.new("RGB", (385 * len(ims), 740), "white")
for i, im in enumerate(ims): W.paste(im, (i * 385, 0))
out = saida / f"prints_{sys.argv[1]}.png"; W.save(out); print(out)
