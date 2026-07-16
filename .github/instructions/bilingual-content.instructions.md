---
applyTo: "**"
---

# Bilingual Content Rule — EN / ES

All content created or modified in this repository **must be written in both English and Spanish**.

## Structure

Use the following format for every file that contains readable prose (README, documentation, descriptions):

```markdown
🇬🇧 [English](#english) · 🇪🇸 [Español](#español)

---

## English

[English content here]

---

## Español

[Spanish content here]
```

## Rules

- **New files**: always include both language sections before committing.
- **Edits**: if you modify content in one language, update the equivalent section in the other language in the same commit.
- **Code files** (`.java`, `.yml`, `.json`, `.sh`, etc.): code itself stays in English; inline comments may be bilingual if they explain complex logic.
- **Git commit messages**: write in English (conventional commits format preferred: `feat:`, `fix:`, `docs:`, `chore:`).
- **Section headers**: use the exact language selector pattern shown above (`🇬🇧 [English](#english) · 🇪🇸 [Español](#español)`) at the top of every bilingual document.
- **Back-links**: footer navigation links must include both languages, e.g. `← [Back to / Volver a](../README.md)`.

## Examples of compliant files

- `README.md` → has `## English` and `## Español` sections.
- `work-experience/README.md` → same bilingual structure with index table.
- `work-experience/globant/README.md` → role/period/location repeated for each language.
