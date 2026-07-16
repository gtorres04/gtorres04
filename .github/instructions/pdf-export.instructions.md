---
description: "Usar SIEMPRE que se pida exportar, generar o convertir a PDF un CV, currículum o cualquier archivo Markdown del repositorio. Indica ejecutar el script scripts/md_to_pdf.py en lugar de improvisar otra herramienta. Trigger: 'exportar a PDF', 'generar PDF', 'convertir a PDF', 'crear PDF del CV'."
applyTo: "cv/**/*.md"
---

# Exportación a PDF

Cuando el usuario pida **exportar / generar / convertir a PDF** un CV, currículum o cualquier `.md` del repositorio, usa **siempre** el script del repo:

```bash
python scripts/md_to_pdf.py <entrada.md> [salida.pdf]
```

Reglas:

- **No improvises** otra herramienta (pandoc, wkhtmltopdf, weasyprint, librerías nuevas, HTML manual, etc.). El método oficial y único es `scripts/md_to_pdf.py`, que ya produce el estilo y formato A4 aprobados.
- Si se omite el PDF de salida, el script usa el mismo nombre del `.md` con extensión `.pdf` (junto al Markdown).
- Para varias variantes, ejecuta el script una vez por archivo (p. ej. la versión ES y la versión EN).
- **Prerrequisitos** (verifícalos o instálalos antes de ejecutar):
  - Python 3.8+ con el paquete `markdown` (`pip install markdown`).
  - Google Chrome, Chromium o Microsoft Edge instalado (el script los detecta automáticamente).
- Si el script falla por falta de `markdown` o de navegador, resuelve el prerrequisito y reintenta; no cambies de herramienta.
- Los PDF resultantes se guardan en `cv/variants/` junto a sus `.md`.

Ejemplo para el CV de energía (ambos idiomas):

```bash
python scripts/md_to_pdf.py cv/variants/cv-software-engineer-java-energia.md
python scripts/md_to_pdf.py cv/variants/cv-software-engineer-java-energia-en.md
```
