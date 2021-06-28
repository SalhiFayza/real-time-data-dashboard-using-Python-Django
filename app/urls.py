
from django.urls import path, re_path
from app import views
app_name = 'app'

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path('fetch_sensor_values_ajax_com', views.fetch_sensor_values_ajax_com,
         name='fetch_sensor_values_ajax_com'),
         
path('fetch_sensor_values_ajax_firebase', views.fetch_sensor_values_ajax_firebase, name='fetch_sensor_values_ajax_firebase'),
    re_path('info.html', views.infos, name='infos'),
    path('show_graph', views.show_graph, name='show_graph'),
    path('data_aquaponics_Humidity', views.data_aquaponics_Humidity, name='data_aquaponics_Humidity'),
    path('data_aquaponics_Temperature', views.data_aquaponics_Temperature, name='data_aquaponics_Temperature'),
    path('data_aquaponics_WaterTemp', views.data_aquaponics_WaterTemp, name='data_aquaponics_WaterTemp'),
    path('data_aquaponics_pH', views.data_aquaponics_pH, name='data_aquaponics_pH'),
    path('getname', views.getname, name='getname'),
    path('get_data_aquaponics_Humidity', views.get_data_aquaponics_Humidity, name='get_data_aquaponics_Humidity'),
    path('get_data_aquaponics_Temperature', views.get_data_aquaponics_Temperature, name='get_data_aquaponics_Temperature'),
    path('get_data_aquaponics_WaterTemp', views.get_data_aquaponics_WaterTemp, name='get_data_aquaponics_WaterTemp'),
    path('get_data_aquaponics_pH', views.get_data_aquaponics_pH, name='get_data_aquaponics_pH'),
    path('read', views.read, name='read'),
    path('get_last_date', views.get_last_date, name='get_last_date'),
   # path('get_data_aquaponics_Humidity_Date', views.get_data_aquaponics_Humidity_Date, name='get_data_aquaponics_Humidity_Date'),
    #path('get_data_aquaponics_Temperature_Date', views.get_data_aquaponics_Temperature_Date, name='get_data_aquaponics_Temperature_Date'),
   # path('get_data_aquaponics_WaterTemp_Date', views.get_data_aquaponics_WaterTemp_Date, name='get_data_aquaponics_WaterTemp_Date'),
   # path('get_data_aquaponics_pH_Date', views.get_data_aquaponics_pH_Date, name='get_data_aquaponics_pH_Date'),
    path('show_graph_com', views.show_graph_com, name='show_graph_com'),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
