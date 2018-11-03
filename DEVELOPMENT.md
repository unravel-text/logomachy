# Development

Set up process:

    pyenv install 3.7.1
    pyenv shell 3.7.1
    python -m venv ~/pyenvs/unravel-text-logomachy
    source ~/pyenvs/unravel-text-logomachy/bin/activate
    pip install --upgrade pip setuptools wheel mypy
    pip install django
    cd ~/Projects/unravel-text-logomachy
    django-admin startproject logomachy_project
    mv ./logomachy_project/* ./
    python manage.py startapp logomachy
    
    pip setuptools mypy
    django docutils psycopg2
    celery django-celery-results django-celery-beat
    django-debug-toolbar django-extensions
    