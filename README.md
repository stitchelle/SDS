# steam-driven-school

##Steps to get the Steam Driven School System started:
* Clone the repo and cd into it

* Create your OSX virtual environment in Terminal:

  * `python -m venv sdsenv`
  * `source ./sdsenv/bin/activate`
  
* Or create your Windows virtual environment in Command Line:

  * `python -m venv workforceenv`
  * `source ./sdsenv/Scripts/activate`
  
* Install the app's dependencies:

  * `pip install -r requirements.txt`
  
* Build your database from the existing models:

  * `python manage.py makemigrations hrapp`
  * `python manage.py migrate`
  
* Create a superuser for your local version of the app:

  * `python manage.py createsuperuser`
  
* Populate your database with initial data from fixtures files: (NOTE: every time you run this it will remove exisiting data and repopulate the tables)

  * `python manage.py loaddata` #Fill this in when you have fixtures!!!!!

* Fire up your dev server and get to work!

  * `python manage.py runserver`
  
## Official SDS LLC ERD
I developed this ERD for you to reference when creating your models.

https://dbdiagram.io/d/5e41d3089e76504e0ef1467b

##Using the Steam Driven School System:

#Fill this in LATER!!!!!
