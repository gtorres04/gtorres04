#!/usr/bin/env python3
"""Genera un PDF a partir de un CV en Markdown.

Convierte un archivo Markdown a HTML con estilo profesional y lo renderiza a
PDF (A4) usando Google Chrome / Chromium en modo headless.

Requisitos:
    - Python 3.8+
    - Paquete `markdown`  ->  pip install markdown
    - Google Chrome, Chromium o Microsoft Edge instalado

Uso:
    python scripts/md_to_pdf.py entrada.md [salida.pdf]

    # Convertir todas las variantes del CV:
    python scripts/md_to_pdf.py cv/variants/cv-software-engineer-java-energia.md
    python scripts/md_to_pdf.py cv/variants/cv-software-engineer-java-energia-en.md

Si se omite el PDF de salida, se usa el mismo nombre del .md con extension .pdf.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CSS = """
@page { size: A4; margin: 14mm 15mm; }
* { box-sizing: border-box; }
body {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  font-size: 10.5px; line-height: 1.5; color: #1a1a1a; margin: 0;
}
h1 { font-size: 22px; margin: 0 0 2px; color: #0b3d5c; }
h1 + p strong { color: #0b6ea8; }
h2 {
  font-size: 13px; text-transform: uppercase; letter-spacing: .5px;
  color: #0b3d5c; border-bottom: 1.5px solid #0b6ea8;
  padding-bottom: 3px; margin: 16px 0 8px;
}
h3 { font-size: 11.5px; margin: 12px 0 3px; color: #12455f; }
p { margin: 4px 0; text-align: justify; }
ul { margin: 4px 0 8px; padding-left: 18px; }
li { margin: 2px 0; }
a { color: #0b6ea8; text-decoration: none; }
strong { color: #0b3d5c; }
hr { border: none; border-top: 1px solid #d8dee4; margin: 10px 0; }
code {
  background: #eef3f7; color: #0b3d5c; padding: 1px 5px;
  border-radius: 3px; font-size: 9.2px; font-family: "SF Mono", Menlo, monospace;
  white-space: nowrap;
}
table { border-collapse: collapse; width: 100%; margin: 6px 0; font-size: 9.5px; }
th, td { border: 1px solid #d8dee4; padding: 4px 6px; text-align: left; vertical-align: top; }
th { background: #0b3d5c; color: #fff; }
tr:nth-child(even) td { background: #f4f7f9; }
blockquote { color: #555; border-left: 3px solid #0b6ea8; margin: 6px 0; padding: 2px 10px; font-size: 9.8px; }
"""

# Rutas/comandos habituales de Chrome/Chromium/Edge por plataforma.
CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "microsoft-edge",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def find_chrome() -> str:
    """Devuelve la ruta ejecutable de Chrome/Chromium/Edge o aborta."""
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists():
            return candidate
        found = shutil.which(candidate)
        if found:
            return found
    sys.exit(
        "ERROR: no se encontro Google Chrome, Chromium ni Microsoft Edge.\n"
        "Instala uno de ellos o edita CHROME_CANDIDATES en el script."
    )


def render_html(md_text: str) -> str:
    try:
        import markdown  # noqa: WPS433 (import diferido a proposito)
    except ImportError:
        sys.exit("ERROR: falta el paquete 'markdown'. Instalalo con: pip install markdown")

    body = markdown.markdown(md_text, extensions=["tables", "sane_lists"])
    return (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )


def md_to_pdf(md_path: Path, pdf_path: Path) -> None:
    if not md_path.is_file():
        sys.exit(f"ERROR: no existe el archivo de entrada: {md_path}")

    html = render_html(md_path.read_text(encoding="utf-8"))
    chrome = find_chrome()

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(html)
        tmp_html = Path(tmp.name)

    try:
        subprocess.run(
            [
                chrome,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                tmp_html.as_uri(),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    finally:
        tmp_html.unlink(missing_ok=True)

    print(f"PDF generado: {pdf_path}")


def main(argv: list[str]) -> None:
    if len(argv) < 2 or argv[1] in {"-h", "--help"}:
        print(__doc__)
        sys.exit(0 if len(argv) >= 2 else 1)

    md_path = Path(argv[1])
    pdf_path = Path(argv[2]) if len(argv) > 2 else md_path.with_suffix(".pdf")
    md_to_pdf(md_path, pdf_path)


if __name__ == "__main__":
    main(sys.argv)
