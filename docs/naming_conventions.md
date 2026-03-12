# Naming Conventions for py-snake

This document captures naming conventions used in the py-snake codebase and the recommended style for new work.

## 1. File Naming

- Use lowercase names for Python files (modules): e.g. `entities.py`, `utils.py`, `combat.py`.
- Use underscores to separate words: `game_state.py`, `player_controller.py`.
- Keep file names short, descriptive, and focused on a single concept or feature.
- Avoid special characters, spaces, or mixed-case in file names.

## 2. Module and Package Names

- Modules should follow file naming rules (lowercase, underscores).
- Package names should also be lowercase with optional underscores for readability.
- Avoid naming modules that conflict with Python standard library modules (e.g., `random.py`, `time.py`).

## 3. Class Naming

- Use PascalCase (CapWords) for class names.
  - Good: `Entity`, `Player`, `Monster`, `GameController`.
  - Bad: `gamecontroller`, `player_class`.

## 4. Function and Variable Naming

- Use snake_case for function and variable names.
  - Good: `slow_print`, `take_damage`, `player_health`.
  - Bad: `slowPrint`, `TakeDamage`, `playerHealth`.
- Keep names readable and meaningful:
  - Use `player_inventory` instead of `p_i`.
  - Use `attack_target` instead of `a`.

## 5. Constants

- Use UPPER_CASE with underscores for constants.
  - Example: `MAX_HEALTH = 100`, `DEFAULT_SPEED = 1.5`.

## 6. Private/Internal Names

- Prefix internal-only attributes/functions with a single underscore.
  - Example: `_connect_database()`, `_current_level`.

## 7. Branch Naming (recommended)

- For feature work: `feat/<short-description>`
- For bugfix work: `fix/<short-description>`
- For refactor: `refactor/<short-description>`
- For docs: `docs/<short-description>`
- For chores: `chore/<short-description>`

Example:
- `feat/player-movement`  
- `fix/enemy-spawn-crash`  
- `docs/add-naming-conventions`

## 8. Git Commit Messages (tie to naming)

- Use Conventional Commit style for commit message header:
  `type(scope): short description`.
- keep scope short (if needed); no abbreviations that obscure meaning.
- Body can include details and references.

This keeps the repo consistent and easy to maintain for future contributors.
