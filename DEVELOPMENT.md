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
    python -m pip --upgrade pip
    
    
Application setup:
    
    python manage.py createsuperuser --username admin --email test@example.com