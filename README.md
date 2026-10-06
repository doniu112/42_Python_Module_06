
# Python Module 06 — The Codex

A 42 Python project about modules, packages, public interfaces, and circular
imports. Small alchemy-themed functions demonstrate how Python resolves imports
and how the same function can be exposed at different package levels.

## Requirements

- Python 3.10 or later.
- No third-party runtime dependencies.
- Optional development tools: `flake8` and `mypy`.

## Getting started

```bash
git clone https://github.com/doniu112/42_Python_Module_06.git
cd 42_Python_Module_06
```

Run the demonstration scripts from the repository root. Package modules that use
relative imports are accessed through these scripts rather than run directly.

## Project structure

| Location | Purpose |
| --- | --- |
| `elements.py` | Fire and water creation functions |
| `alchemy/elements.py` | Earth and air creation functions |
| `alchemy/__init__.py` | Public package exports and the `heal` alias |
| `alchemy/potions.py` | Healing and strength potions composed from element functions |
| `alchemy/transmutation/recipes.py` | A lead-to-gold recipe using absolute and relative imports |
| `alchemy/transmutation/__init__.py` | Exposes `lead_to_gold` through the subpackage |
| `alchemy/grimoire/light_spellbook.py` | Light spell ingredients and recording |
| `alchemy/grimoire/light_validator.py` | Ingredient validation with a deferred import |
| `alchemy/grimoire/dark_spellbook.py` | Spellbook participating in an intentional circular import |
| `alchemy/grimoire/dark_validator.py` | The other side of the intentional circular import |
| `alchemy/grimoire/__init__.py` | Exposes the working light spell interface |

## Part I — Alembic

Six scripts demonstrate module imports, direct function imports, and package
exports.

| Script | Demonstration |
| --- | --- |
| `ft_alembic_0.py` | `import elements` and fire creation |
| `ft_alembic_1.py` | `from elements import create_water` |
| `ft_alembic_2.py` | `import alchemy.elements` and earth creation |
| `ft_alembic_3.py` | Direct import of `create_air` from `alchemy.elements` |
| `ft_alembic_4.py` | Public `alchemy.create_air` and intentionally unavailable `alchemy.create_earth` |
| `ft_alembic_5.py` | `from alchemy import elements` and air creation |

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py
python3 ft_alembic_5.py
```

`ft_alembic_4.py` intentionally raises an uncaught `AttributeError` and exits
with a nonzero status. The earth function exists in `alchemy.elements`, but is
not exported as `alchemy.create_earth`. This is a required demonstration.

## Part II — Distillation

The potion functions combine results from the element functions:

- `healing_potion()` uses earth and air.
- `strength_potion()` uses fire and water.
- `alchemy.heal` is an alias for `healing_potion`.

```bash
python3 ft_distillation_0.py
python3 ft_distillation_1.py
```

The first script imports the functions directly from `alchemy.potions`. The
second accesses the public functions through `import alchemy`.

## Part III — Transmutation

`lead_to_gold()` composes a recipe from air, a strength potion, and fire.
Its module combines an absolute import (`from elements import create_fire`)
with relative imports (`from ..elements ...` and `from ..potions ...`).

```bash
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
```

These scripts access the same function through three interfaces:

1. `alchemy.transmutation.recipes.lead_to_gold()`
2. `alchemy.transmutation.lead_to_gold()`
3. `alchemy.lead_to_gold()`

## Part IV — Grimoire

The light spellbook accepts an ingredient string when it contains at least one
of `earth`, `air`, `fire`, or `water`. Matching is case-insensitive and uses
substring membership. Empty strings and strings without a matching ingredient
are rejected.

The light validator imports the allowed-ingredients function inside
`validate_ingredients()`. This delays the import until the spellbook has
finished initializing and allows both modules to work together.

```bash
python3 ft_kaboom_0.py
```

Example output:

```text
=== Kaboom 0 ===
Spell recorded: Fantasy (Earth, wind and fire - VALID)
Spell rejected: Unknown (sand and salt - INVALID)
```

The dark modules declare `bats`, `frogs`, `arsenic`, and `eyeball` as allowed
ingredients, but intentionally import each other at module level. Importing
the dark spellbook fails before a spell can be recorded.

```bash
python3 ft_kaboom_1.py
```

This script catches the expected `ImportError` and prints its message. It
therefore exits normally even though the import failed. The circular dependency
is intentional and should be preserved for this exercise. The `grimoire`
package exports only the light recording function so the dark example does not
prevent the light example from working.

## Code checks

Install the optional tools and run them from the repository root:

```bash
python3 -m pip install flake8 mypy
python3 -m flake8 .
python3 -m mypy .
python3 -m mypy --strict .
```

The type-checking error for `alchemy.create_earth()` in `ft_alembic_4.py` is
intentional. Other diagnostics should be addressed. A caught runtime circular
import is demonstrated separately by `ft_kaboom_1.py`.

## Concepts practiced

- Absolute and relative imports.
- Modules versus packages and subpackages.
- Package initialization through `__init__.py`.
- Explicit public exports through `__all__`.
- Import aliases and re-exporting functions.
- Circular dependencies and deferred imports.
- Type annotations and static code checks.
