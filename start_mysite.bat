call .\venv\Scripts\activate.bat
cd .\mysite
python manage.py makemigrations
python manage.py migrate
python .\manage.py runserver 0.0.0.0:8000
pause