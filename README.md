# real-time-data-dashboard-using-Python-Django
Dashboard (local website) to constitute and display the data of the sensors on the interfaces in the form of values and curves.
# USING:
- Software: VSCode.
- Language: back-end and front-end: Python, Django, Ajax, HTML, CSS, JavaScript, Bootstrap.
- DB: Firebase.
- DB: sqlite3.
- Django: is an open-source web development framework in Python.
- Lib Django: pip install django.
# Create project django:

**- To create a Django project:**

- django-admin satrtproject name _projrct .

**- To create a Django app:**

- python manage.py startapp name_app .

**- Start the server:**

- python manage.py runserver.

**- Stop the server:**

- CTRL+C.

**- Run the test:**

- python manage.py test.

**- Create user:**

- python manage.py createsuperuser.

**- Create the migrations(generate the SQL commands):**

- python manage.py makemigrations posts.

**- Run the migrations(execute the SQL commands):**

- python manage.py migrate posts.

# Create Account Firebase.

- Create account 

- Create project

- Link  a Project-Firebase for your Project Django:

with code configiration:

// For Firebase JS SDK v7.20.0 and later, measurementId is optional

const firebaseConfig = {

  apiKey: "******************",
  
  authDomain: "*********************",
  
  databaseURL: "***********************",
  
  projectId: "***********",
  
  storageBucket: "**************",
  
  messagingSenderId: "***********",
  
  appId: "******",
  
  measurementId: "********"
  
};

- add the code conf in <scripts></scripts> or in the views.py or in the file JSON.

# GET-POST Data RealTime Firebase and Serial

- how to plot live/real-time graphs using python from Arduino connected with any sensors and display in web applications(Django).

- how to plot live/real-time graphs using python from Firebase connected with data and display in web applications(Django).

- Using Ajax: is a method using different technologies added to web browsers.

- AJAX(asynchronous JavaScript and XML ).

- Libs Using:
asgiref==3.2.3
certifi==2019.11.28
chardet==3.0.4
dj-database-url==0.5.0
Django==3.0.1
django-heroku==0.3.1
gunicorn==20.0.4
heroku==0.1.4
idna==2.8
psycopg2==2.8.4
python-dateutil==1.5
pytz==2019.3
requests==2.22.0
sqlparse==0.3.0
urllib3==1.25.7
whitenoise==5.0.1

# Local SiteWeb
* Form data in Firebase: Overview of the web application:

![image](https://user-images.githubusercontent.com/60444937/126646168-47730218-a06a-40ef-be8b-dadd420305e8.png)

* Part 1: Authentification with SQLite(data base Django). 

![90](https://user-images.githubusercontent.com/60444937/126646643-703fe89e-12b1-4cd4-acb7-666d6b1fb06a.PNG)![91](https://user-images.githubusercontent.com/60444937/126646628-2ce52d36-41cd-4e55-aa1f-b4a17d8a417c.PNG)

* Part 2: Data Firebase(Home):


![92](https://user-images.githubusercontent.com/60444937/126647540-1fc1e97d-e90b-4931-9bbd-ff7c6854e1d2.PNG)



