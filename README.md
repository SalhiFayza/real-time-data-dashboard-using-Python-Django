# real-time-data-dashboard-using-Python-Django
Web server using an "Arduino UNO+Raspberry Pi" and DHT22, DS18B20, Pro SKU SEN0169 sensors to graph the data in my Aquaponics over time. The data can be accessed over a web browser.
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

# Django codebase structure

                    < PROJECT ROOT >
                       |
                       |-- core/                               # 
                       |    |-- static/                        #  
                       |    |    |-- <css, JS, images>         # CSS files
                       |    |
                       |    |-- templates/                     # Templates
                       |         |
                       |         |-- includes/                 # HTML 
                       |         |    |-- navigation.html      # Top menu component
                       |         |    |-- sidebar.html         # Sidebar component
                       |         |    |-- footer.html          # App Footer
                       |         |    |-- scripts.html         # JS Scripts 
                       |         |
                       |         |-- layouts/                  # Master pages
                       |         |    |-- base-fullscreen.html # 
                       |         |    |-- base.html            # 
                       |         |
                       |         |-- accounts/                 # Authentication pages
                       |         |    |-- login.html           # Login page
                       |         |    |-- register.html        # Register page
                       |         |
                       |      index.html                       # The default page
                       |     page-404.html                     # Error 404 page
                       |     page-500.html                     # Error 404 page
                       |       *.html                          # All other HTML pages
                       |
                       |-- authentication/                     # Handles auth routes
                       |
                       |-- app/                                # Serve HTML files
                       |    
                       |
                       |-- requirements.txt                    # App Dependencies
                       |
                       |-- .env                                # Inject Environment 
                       |-- manage.py                           # Start the app 
                       |
                       |-- *********************************************************
   
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

Here I use an (Arduino UNO+Raspberry Pi) and a DHT22, DS18B20, Pro SKU SEN0169 sensors, combined with a python virtual environment and SQLite, to store data from my Aquaponics and display it in a web server.

I use Django and AJAX for the Django webserver. 
Python and Ajax to take data Firebase and store the data in an SQLite database. I also include a link to Plotly.

* Form data in Firebase: Overview of the web application:

![image](https://user-images.githubusercontent.com/60444937/126646168-47730218-a06a-40ef-be8b-dadd420305e8.png)

* Part 1: Authentification with SQLite(data base Django). 

![90](https://user-images.githubusercontent.com/60444937/126646643-703fe89e-12b1-4cd4-acb7-666d6b1fb06a.PNG)![91](https://user-images.githubusercontent.com/60444937/126646628-2ce52d36-41cd-4e55-aa1f-b4a17d8a417c.PNG)

* Part 2: Data Firebase"Home":

![92](https://user-images.githubusercontent.com/60444937/126647540-1fc1e97d-e90b-4931-9bbd-ff7c6854e1d2.PNG)

* Part 3: Data SQLite(DB Django)"Data":

Interface of stored curves.

In this interface, storing aquaponics data in the Django database and displaying it as curves.

To access the curves for a specific date, simply click in the calendar displayed in the interface and choose the desired date and the curves will be displayed as shown in the following figure.

(1):

![ttttttttttttttttttttt](https://user-images.githubusercontent.com/60444937/126651331-cd06ceec-3fb6-45bf-8de1-32efaf0a0ef1.PNG)

(2):

 ![9548](https://user-images.githubusercontent.com/60444937/126653841-fb3237b6-343f-4306-920d-a11027068ec3.PNG)
 
(3):

![6](https://user-images.githubusercontent.com/60444937/126652310-a36bcab4-f613-4ff3-84a7-6a9c500c7d33.PNG)

(4):

![9](https://user-images.githubusercontent.com/60444937/126652509-1f5440dd-806a-4643-ad50-d1e8ef84d361.PNG)![10](https://user-images.githubusercontent.com/60444937/126652551-562b6ee6-cfab-4777-98f5-7b50be26b9be.PNG)![11](https://user-images.githubusercontent.com/60444937/126652567-3e1dd2a5-d86d-4a25-ae22-6b2a9cf33605.PNG)![12](https://user-images.githubusercontent.com/60444937/126652593-7746571d-471f-4667-81b9-770b4d465646.PNG)

* Part 3: Data Firebase"Charts for data firebase":

This interface displays the different curves of aquaponics data (humidity, temperature, water temperature and pH) using the Firebased database as shown in the following figures:

![94](https://user-images.githubusercontent.com/60444937/126654066-7844f593-8440-494a-b558-0d883c7672c7.PNG)
![95](https://user-images.githubusercontent.com/60444937/126654082-dff74bf4-329c-4292-937b-f0b225b824c8.PNG)
![96](https://user-images.githubusercontent.com/60444937/126654103-d7fa1926-f518-4815-9a0d-64bd69beef23.PNG)
![5](https://user-images.githubusercontent.com/60444937/126654662-95d792a4-c989-4ba2-bc44-d77b60f7541d.PNG)

* Part 4: Settings:

This interface allows the administrator to change the temperature threshold according to the studies carried out and the ambient temperature in aquaponics.

![a](https://user-images.githubusercontent.com/60444937/126655048-ccfd0da4-69b7-4f18-b6f3-dab8eb657609.PNG)
