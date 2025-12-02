# djeopardy — Jeopardy-style Django sample app

A small Django project that implements a simple poll/jeopardy UI. This README explains how to set up, run, and test the project locally and documents the recent UI enhancement that adds a 3D rotating fade-in effect to the question display.

## Overview

- Django-based sample application. The `polls` app contains models for Questions, Choices and Categories and a custom `jeopardy` view that renders a Jeopardy-style board (see `polls/templates/polls/jeopardy.html`).
- Database: SQLite (file `db.sqlite3` in repository root).
- This repository was built with Django 5.2.8 (see `mysite/settings.py`).

## Prerequisites

- Python 3.9+ (recommended). The code was developed for Django 5.2.x — using Django 5.2.8 is recommended for parity with the project settings.
- Git (optional, for cloning or branching).

## Quick setup (local development)

1. Clone or open the repo and change into the project root (where `manage.py` lives):

```powershell
cd C:\path\to\repo\mysite
```

2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install Django (pin recommended to match the project settings). If you need to install additional dependencies, add them to a `requirements.txt` file.

```powershell
pip install Django==5.2.8
```

4. Run database migrations (the project uses SQLite so no DB server is required):

```powershell
python .\manage.py migrate
```

5. (Optional) Create a superuser to access the Django admin and add/edit `Question` / `Category` data:

```powershell
python .\manage.py createsuperuser
```

6. Start the development server:

```powershell
python .\manage.py runserver
```

7. Open the app in your browser:

- Default root index: http://127.0.0.1:8000/polls/
- Jeopardy board: http://127.0.0.1:8000/polls/jeopardy

## Project structure (high-level)

- `manage.py` — Django management utility
- `mysite/` — Django project settings + WSGI/ASGI
- `polls/` — app with models, views, templates, and admin configuration
- `db.sqlite3` — SQLite DB file (committed here for example/dev)

## Tests

Run tests using Django's test runner:

```powershell
python .\manage.py test
```

## Notes about the Jeopardy UI and recent changes

- The `jeopardy` view is defined in `polls/views.py` and uses template `polls/templates/polls/jeopardy.html`.
- A 3D rotating fade-in animation was added to the question overlay. The animation is implemented directly in the `jeopardy.html` file (in the `<head>` styles) and is triggered by simple JavaScript when a user clicks a question tile.
- Key details:
  - The wrapper `#question-display` now sets a CSS `perspective` so child `.big-question` elements animate with a 3D rotateY effect.
  - The animation makes the question rotate in from the right and fade up into view using `@keyframes fadeRotateIn`.
  - For safety, question text is inserted using a DOM text node (via `textContent`) — this prevents accidental HTML injection. The template also uses `|escapejs` to safely embed question text into inline `onclick` handlers.
