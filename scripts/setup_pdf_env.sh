#!/usr/bin/env bash
#
# Prepara el entorno para ejecutar scripts/md_to_pdf.py.
#
# Muchos sistemas (p. ej. macOS con Homebrew) traen un Python "externally
# managed" (PEP 668) donde `pip install markdown` falla. Este script crea un
# entorno virtual aislado en `.venv/` e instala la dependencia `markdown`,
# dejando todo listo para generar los PDFs sin tocar el Python del sistema.
#
# Uso:
#   ./scripts/setup_pdf_env.sh
#
# Después, genera los PDFs con el Python del venv:
#   .venv/bin/python scripts/md_to_pdf.py cv/variants/<archivo>.md
#
set -euo pipefail

# Raíz del repositorio (carpeta que contiene este script/../).
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${REPO_ROOT}/.venv"

# Detecta un intérprete de Python 3.
PYTHON_BIN=""
for candidate in python3 python; do
  if command -v "${candidate}" >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v "${candidate}")"
    break
  fi
done

if [[ -z "${PYTHON_BIN}" ]]; then
  echo "ERROR: no se encontró Python 3. Instálalo y reintenta." >&2
  exit 1
fi

# Crea el venv si aún no existe.
if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
  echo "Creando entorno virtual en ${VENV_DIR} ..."
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
fi

# Instala/actualiza la dependencia necesaria dentro del venv.
echo "Instalando dependencia 'markdown' ..."
"${VENV_DIR}/bin/python" -m pip install --quiet --upgrade pip markdown

echo ""
echo "Entorno listo. Genera los PDFs con:"
echo "  ${VENV_DIR}/bin/python scripts/md_to_pdf.py cv/variants/<archivo>.md"
