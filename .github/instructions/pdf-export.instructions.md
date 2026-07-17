---
description: "Usar SIEMPRE que se pida exportar, generar o convertir a PDF un CV, currículum o cualquier archivo Markdown del repositorio. Indica ejecutar el script scripts/md_to_pdf.py en lugar de improvisar otra herramienta. Trigger: 'exportar a PDF', 'generar PDF', 'convertir a PDF', 'crear PDF del CV'."
applyTo: "cv/**/*.md"
---

# Exportación a PDF

Cuando el usuario pida **exportar / generar / convertir a PDF** un CV, currículum o cualquier `.md` del repositorio, usa **siempre** el script del repo:

```bash
python scripts/md_to_pdf.py <entrada.md> [salida.pdf]
```

## Preparación del entorno (obligatoria la primera vez)

Antes de ejecutar `md_to_pdf.py`, prepara el entorno con el script de setup del repo:

```bash
./scripts/setup_pdf_env.sh
```

Este script crea un entorno virtual aislado en `.venv/` e instala la dependencia
`markdown`, evitando el error de "externally managed environment" (PEP 668) que
aparece en sistemas como macOS con Homebrew. Tras ejecutarlo, genera los PDFs
usando el Python del venv:

```bash
.venv/bin/python scripts/md_to_pdf.py <entrada.md> [salida.pdf]
```

- Ejecuta `./scripts/setup_pdf_env.sh` **una sola vez** (o de nuevo si borras `.venv/`); es idempotente.
- **No instales** `markdown` con `pip install --break-system-packages` ni sobre el Python del sistema: usa siempre el venv creado por el script de setup.
- La carpeta `.venv/` está en `.gitignore` y **no** debe commitearse.

## Reglas

- **No improvises** otra herramienta (pandoc, wkhtmltopdf, weasyprint, librerías nuevas, HTML manual, etc.). El método oficial y único es `scripts/md_to_pdf.py`, que ya produce el estilo y formato A4 aprobados.
- Si se omite el PDF de salida, el script usa el mismo nombre del `.md` con extensión `.pdf` (junto al Markdown).
- Para varias variantes, ejecuta el script una vez por archivo (p. ej. la versión ES y la versión EN).
- **Prerrequisitos** (verifícalos o instálalos antes de ejecutar):
  - Entorno preparado con `./scripts/setup_pdf_env.sh` (Python 3.8+ con el paquete `markdown` dentro de `.venv/`).
  - Google Chrome, Chromium o Microsoft Edge instalado (el script los detecta automáticamente).
- Si el script falla por falta de `markdown`, ejecuta `./scripts/setup_pdf_env.sh` y reintenta; si falla por navegador, resuelve ese prerrequisito. No cambies de herramienta.
- Los PDF resultantes se guardan en `cv/variants/` junto a sus `.md`.

Ejemplo para el CV de energía (ambos idiomas):

```bash
./scripts/setup_pdf_env.sh
.venv/bin/python scripts/md_to_pdf.py cv/variants/cv-software-engineer-java-energia.md
.venv/bin/python scripts/md_to_pdf.py cv/variants/cv-software-engineer-java-energia-en.md
```
