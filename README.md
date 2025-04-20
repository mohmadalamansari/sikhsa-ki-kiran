firstly clone 
goto that file 

than follow from step 3
python -m venv env

env\Scripts\activate

pip install -r requirements.txt  # or pip install django if no file

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
