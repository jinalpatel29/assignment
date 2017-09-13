# assignment
credit card  API that simulates money  transaction events

Supports Django REST Framework Serializers

Requirements
This module is tested and work with:
Python 2.7
Django 1.11
Django REST Framework 3.6.4

If you dont have these software already then please install it
You can verify it by running pip freeze in your command prompt

Installation:
1) Download python from https://www.python.org/downloads/
 then run python -V in cmd , it will shows version like Python 2.7.13
2) pip install django
3) pip install djangorestframework

STEPS:
1) Checkout the folder from GIT repository
2) if you are using windows then open cmd and go to the directory where you have saved the project and goto creditcard where you find manage.py in folder
3) then run command    python manage.py runserver 
4) Now server should be up and running you can hit the URL http://localhost:8000/health/
4) Please use postman - to test API, if you do not have it then please install it first.

Note : I have used sqllite database provided by Django framework and stored data into that only. 
We can add our own database like mysql if we would like for now, I have done with sqllite

