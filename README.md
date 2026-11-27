# French Verb Trainer

This program is a French verb conjugation trainer.
Language learners need regular practice with verb forms, which are one of the
most error-prone parts of French grammar. This application generates random
conjugation exercises and checks the user's answers, providing an endless
practice loop without unnecessary complexity. The current prototype uses a
console interface; a graphical interface is planned.

## Key Features

- **Random Exercise Generation**: generates an unlimited number of exercises from a built-in verb set
- **Tense and Subject Variety**: random combinations of tense and subject pronouns
- **Answer Checking**: tolerant comparison of user answers (case-insensitive, leading/trailing whitespace ignored)
- **Layered Architecture**: interface → services → repositories → models, with dependencies injected between layers
- **Extensible Verb Base**: verbs stored as dataclasses; the repository layer abstracts storage, allowing backends to be swapped later

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SabirovaLilia/PFL_final_project.git
   cd PFL_final_project
   ```

2. Install [uv](https://docs.astral.sh/uv/) and sync dependencies
   (Python 3.13+ required):

   ```bash
   uv sync --locked
   ```

## Usage

Run the trainer:

```bash
uv run python -m french_verb_trainer.main
```

The application asks to conjugate a random verb; type your answer and press
Enter, or `q` to quit.

## Testing

```bash
uv run pytest
```

## Pre-commit

Pre-commit runs code checks automatically before each commit: Ruff lint and
format, pytest, and basic file hygiene (trailing whitespace, end of files,
yaml/toml validity, merge conflict markers, private keys).

After cloning the repository, run:

```bash
uv tool install pre-commit==4.7.0
pre-commit install
pre-commit run --all-files
```

## Architecture

The application follows a layered architecture: Interface (package `gui`,
console prototype) → Services (exercise generation, answer checking) →
Repositories (verb storage) → Models (`Verb`, `Exercise` dataclasses).

## Contributors

- Doroshina Aleksandra ([github.com/DoroshinaAleksandra](https://github.com/DoroshinaAleksandra))
- Evgrafova Anna ([github.com/Evgraff2005](https://github.com/Evgraff2005))
- Sabirova Lilia ([github.com/SabirovaLilia](https://github.com/SabirovaLilia))
