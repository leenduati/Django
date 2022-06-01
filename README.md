# Django - Ubuntu Debian 20.02
This is a Django Course, with snippets from Jose Portilla's Course in Udemy

Virtual Environments are important in Django installations. They assist the user to keep up with Packages updates in Django. I have used Conda as a virtual environment (venv) in this course.
Install conda by sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
Then Update by: conda update --all
Create a virtual environment by: conda create --name MyEnv django
This will install all libraries and django instance
Then activate by: conda activate myEnv
Deactivate by: conda deactivate myEnv

List all venv by: conda env list

Install Django with: conda install django
when you install Django, it actually also installed a command line tool called: django-admin

Create first project with: django-admin startproject first_project


The following packages will appear after creation:
1. __init.py__ Blank Python Script that treats directory as a package
2. settings.py Stores project settings
3. urls.py stores URL patterns for the project
4. wsgi.py Web Server Gateway Interface. Help us deploy our web app to production
5. manage.py We will wite our web applications here.

Run: python manage.py runserver to create a server environment after running python manage.py migrate
localserver env at 127.0.0.1:8000 will be initiated
Migrations: This has to do with databases and how to connect them to Django. A migration allows you to move databases from one design to another - it is reversible
A Django Project is a collection of applications and configurations that when combined together will make up the full web app
A DJango app is created to perform a particular functionality for your entire web app.
create a django aplication with: python manage.py startapp first_app

A folder with first_app will be created:
1. __init.py__ blank Python script that allows directory to be treated as a package
2. admin.py register models which will then be used with Django's admin interface
3. apps.py Here you can place app specific configs
4. models.py Storing application data models
5. tests.py Store test functions for testing
6. views.py Functions that handle requests and return responses
7. migrations folder: stores database specific info as it relates to the models

In the projectname/settings.py file will add first_app to INSTALLED APPS LIST VARIABLE!

In views.py under first_app, add code, from django.http import HttpResponse

map the view to uls.py file under first project
urlpatterns = [
    path('', views.index, name="hello"),
    path('admin/', admin.site.urls),
]

# Challenge Lecture
Complete the following tasks:
1. Create a New Django Project: ProTwo
2. Create a New Django App: AppTwo
3. Create an INdex View that returns:
        <em>My Second App </em>
4. Link this view to the urls.py file