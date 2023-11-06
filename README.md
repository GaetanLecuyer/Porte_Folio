# Mon Projet Django

## Installation

```bash
git clone https://github.com/votreutilisateur/mon-projet-django.git
cd mon-projet-django
python -m venv venv
source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

