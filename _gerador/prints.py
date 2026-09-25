"""Capturas de tela de todas as rotas de um MVP, lado a lado — para revisão visual.
Uso: py _gerador/prints.py Grupo1  -> salva em %TEMP%/claude/prints_<grupo>/folha.png"""
import subprocess, sys, tempfile
from pathlib import Path
RAIZ = Path(__file__).resolve().parent.parent
alvo = next(RAIZ.glob(f"{sys.argv[1]}*/app.html"))
saida = Path(tempfile.gettempdir()) / "claude" / f"prints_{sys.argv[1]}"
subprocess.call([sys.executable, str(RAIZ.parent / "_ferramentas/smoke.py"), f"8AdmVG/{alvo.parent.name}/app.html", "--shots", str(saida)])
