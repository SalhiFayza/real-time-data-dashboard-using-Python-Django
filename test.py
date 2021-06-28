import os, sys
from firebase import firebase
from datetime import datetime
import time
sys.path.append('C:/Users/SalhiFayza/pfe2021_dash/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
import django
django.setup()
from app.models import Foo
while True:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    aa = firebase.FirebaseApplication(
                    'https://aquaponicsapp-d4dda-default-rtdb.firebaseio.com/', None)
    result = aa.get('/DATA/', '')
    humidity = result.get('Humidity').get('Data')
    temperature = result.get('Temperature').get('Data')
    WaterTemp = result.get('WaterTemp').get('Data')
    ph = result.get('pH').get('Data')
    foo_instance = Foo.objects.create(ph=str(ph).split(" ")[1],humdit=str(humidity).split(" ")[1],waterTemp=str(WaterTemp).split(" ")[1],temp=str(temperature).split(" ")[1])
    print("Done Adding Data {}".format(current_time))
    time.sleep(900)