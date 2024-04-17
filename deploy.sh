#!/bin/bash     
sudo git pull origin main
source .venv/bin/activate
sudo pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
deactivate
sudo systemctl restart nginx
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
