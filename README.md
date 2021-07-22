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

-Create account 

-Create project

-Link  a Project-Firebase for your Project Django:

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

-add the code conf in <scripts></scripts> or in the views.py or in the file JSON.
