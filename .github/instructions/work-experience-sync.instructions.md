---
applyTo: "work-experience/**/README.md"
---

# Work Experience Sync Rule

Whenever a **new work experience is created or an existing one is significantly modified** (new company/project folder under `work-experience/<slug>/README.md`), the following updates are **mandatory in the same change**:

## 1. Update `work-experience/README.md`

- Add (or update) a row in the **Experience Index / Índice de Experiencias** table:
  `| [Company](slug/README.md) | Role | Period |`
- Order rows from most recent to oldest (top = most recent / ongoing).
- If the new experience is relevant enough to shift the overall narrative (e.g., new primary stack, new domain, freelance vs full-time), update the **Summary / Extracto** section at the top of this file (both `## English` and `## Español`) to reflect it, following the bilingual rule.

## 2. Propose an update to the main profile `README.md` (repo root, `gtorres04/README.md`)

Based on the tech stack and role of the new experience, **propose** (do not silently rewrite) changes to:

- The **"I'm currently working on" / "Actualmente trabajo en"** bullet, if the new experience is the current/most recent one.
- The **"I'm currently learning" / "Actualmente aprendo"** bullet, if the new stack introduces technologies not yet listed.
- The **🛠️ Technologies & Tools / Tecnologías y herramientas** section, adding any new languages, frameworks, data stores, messaging systems, cloud providers, CI/CD, observability, or IaC tools introduced by the new experience that aren't already listed.

Always present these proposed changes to the user for confirmation before applying them, since the main README is a curated personal summary, not an auto-generated index.

## Rules

- Never add a new `work-experience/<slug>/README.md` without also updating the index table in `work-experience/README.md` in the same commit.
- Keep both the table entry and any summary changes bilingual (EN/ES), per the bilingual content rule.
- Company/project folder slugs use kebab-case (e.g., `masorange`, `grupo-ditech`).
