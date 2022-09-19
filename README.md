# SMAL-PM-SYSTEM
A simple project management system using Django as a backend and SQLite as a storage.

See the list of projects, milestones and respective completion dates. 


# Setup
1. Install Django in virtual environment `pip install -r requirements.txt`
2. Execute migrations `python manage.py migrate`
3. Load initial data `python manage.py loaddata data.json`
4. Start the server `python manage.py runserver`


Admin account credentials: 
- user: "smalmanager", pass: "smalpassword"
- or run `python manage.py createsuperuser`



