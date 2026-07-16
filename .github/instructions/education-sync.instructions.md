---
applyTo: "education/**/README.md"
---

# Education Sync Rule

Whenever a **new education entry is created or an existing one is significantly modified** (new institution/program folder under `education/<slug>/README.md`), the following updates are **mandatory in the same change**:

## 1. Update `education/README.md`

- Add (or update) a row in the **Education Index / Índice de Educación** table:
  `| [Institution](slug/README.md) | Degree | Period |`
- Order rows from most recent to oldest (top = most recent).
- If the new entry is relevant enough to shift the overall narrative (e.g., a new degree level, a new field of study), update the **Summary / Extracto** section at the top of this file (both `## English` and `## Español`) to reflect it, following the bilingual rule.

## 2. Propose an update to the main profile `README.md` (repo root, `gtorres04/README.md`)

Based on the degree and field of the new education entry, **propose** (do not silently rewrite) changes to:

- The **📄 More details / Más detalles** section, ensuring the `Education / Educación` link is present.
- Any bullet or skills section where the new academic background is relevant enough to mention (e.g., a specialization that reinforces the professional narrative).

Always present these proposed changes to the user for confirmation before applying them, since the main README is a curated personal summary, not an auto-generated index.

## Rules

- Never add a new `education/<slug>/README.md` without also updating the index table in `education/README.md` in the same commit.
- Keep both the table entry and any summary changes bilingual (EN/ES), per the bilingual content rule.
- Institution/program folder slugs use kebab-case (e.g., `politecnico-grancolombiano`, `comfenalco-especializacion-ingenieria-software`).
- When the same institution appears in more than one entry, disambiguate the slug by appending the program (e.g., `comfenalco-tecnologia-sistemas` vs `comfenalco-especializacion-ingenieria-software`).
