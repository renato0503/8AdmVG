"""Teste de fumaça dos 5 MVPs (app.html) em 375x740 — usa o testador genérico _ferramentas/smoke.py.

Cada MVP tem arquitetura própria e expõe `window.__rotas`; o testador percorre as rotas, clica em
todos os botões visíveis, e reprova se houver erro de JS ou rolagem horizontal; também confere se o
estado salvo sobrevive ao recarregar.

Uso (da raiz 8AdmVG):  py _gerador/testar_apps.py [filtro] [--shots <pasta>]
"""
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
args = sys.argv[1:]
filtro = args[0] if args and not args[0].startswith("--") else ""
extra = args[1:] if filtro else args
apps = [f"8AdmVG/{p.parent.name}/app.html" for p in sorted(RAIZ.glob("Grupo*/app.html")) if filtro in p.parent.name and "RotaViva" not in p.parent.name]
sys.exit(subprocess.call([sys.executable, str(RAIZ.parent / "_ferramentas/smoke.py"), *apps, "8AdmVG/coleta/index.html", *extra]))
