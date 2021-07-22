
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.shortcuts import render
from firebase import firebase
from django.http import HttpResponse, JsonResponse
import random
import serial
import sqlite3
import json
from django.views.decorators.csrf import csrf_protect
from tkinter import *
from sqlite3 import Error
from datetime import datetime, timedelta
import plotly.graph_objs as go
import cufflinks as cf
import  plotly.offline as opy
import time
from .forms import NameForm

@login_required(login_url="/login/")
def index(request):
    aa = firebase.FirebaseApplication(
        '***************************************', None)
    result = aa.get('/DATA/', '')
    return render(request, 'index.html', {'result': result})


@login_required(login_url="/login/")
def infos(request):
    aa = firebase.FirebaseApplication(
        '***************************************', None)
    result = aa.get('/DATA/', '')
    return render(request, 'info.html', {'result': result})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-403.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def show_graph(request, template_name='charts-morris.html'):
    return render(request, template_name)
#******************************** for serial arduino
def show_graph_com(request, template_name='live.html'):
    return render(request, template_name)
def fetch_sensor_values_ajax_com(request):
    data={}
    if request.is_ajax():
            sensor_data0=[]
            sensor_val=random.random()
            try:
                ser=serial.Serial("COM3",9600)
                ser_bytes = ser.readline().decode().strip().split(',')
                new_ser_bytes = [float(i) for i in ser_bytes]
                now=datetime.now()
                ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
                humidity = new_ser_bytes[0]
                temperature = new_ser_bytes[1]
                WaterTemp =new_ser_bytes[2]
                ph =new_ser_bytes[3]
                if humidity is not None and temperature is not None and WaterTemp is not None and ph is not None:
                    sensor_data0.append(str(humidity)+','+ok_date)
                    sensor_data0.append(str(temperature)+','+ok_date)
                    sensor_data0.append(str(WaterTemp)+','+ok_date)
                    sensor_data0.append(str(ph)+','+ok_date)
                    x=sensor_data0
                else:
                    sensor_data0.append(str(sensor_val)+','+ok_date)
            except Exception as e:
                    sensor_data0.append(str(sensor_val)+','+ok_date)
            data['result']=x
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)
#********************************************************************************************    
def fetch_sensor_values_ajax_firebase(request):
    data = {}
    if request.is_ajax():
        print("req is ajax \n")

        sensor_data0 = []
        try:
            print("trying to fetch \n")
            aa = firebase.FirebaseApplication(
                '******************************', None)
            result = aa.get('/DATA/', '')
            now = datetime.now()
            ok_date = str(now.strftime('%Y-%m-%d %H:%M:%S'))
            humidity = result.get('Humidity').get('Data')
            temperature = result.get('Temperature').get('Data')
            WaterTemp = result.get('WaterTemp').get('Data')
            ph = result.get('pH').get('Data')
            sensor_data0.append(str(humidity).split(" ")[1]+','+ok_date)
            sensor_data0.append(str(temperature).split(" ")[1]+','+ok_date)
            sensor_data0.append(str(WaterTemp).split(" ")[1]+','+ok_date)
            sensor_data0.append(str(ph).split(" ")[1]+','+ok_date)
            data = sensor_data0

        except Exception as e:
            print("error \n"+e)

            pass
    else:
        data = 'Not Ajax'
    return JsonResponse(data, safe=False)
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("db.sqlite3")
    except Error as e:
        print(e)

    return conn
def store_data(conn, project):
    sql = ''' INSERT INTO data_aquaponics(id,data,date,type)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
def data_aquaponics_Humidity(request):
    if request.method=='POST' :
        id=request.POST['id']
        data=request.POST['data']
        date=request.POST['date']
        type=request.POST['type']
        print("data   ", data, sep=" : --****- :")
        print("date ", date, sep=": -****-- :")
        print("id ", id, sep=": --**- :")
        print("type ", type, sep=": --**- :")
        json_data=(id,data,date,type)
        conn = create_connection()
        with conn:
            store_data(conn,json_data)
    return HttpResponse("OK")
def data_aquaponics_Temperature(request):
    if request.method=='POST' :
        id=request.POST['id']
        data=request.POST['data']
        date=request.POST['date']
        type=request.POST['type']
        print("data   ", data, sep=" : --****- :")
        print("date ", date, sep=": -****-- :")
        print("id ", id, sep=": --**- :")
        print("type ", type, sep=": --**- :")
        json_data=(id,data,date,type)
        conn = create_connection()
        with conn:
            store_data(conn,json_data)
    return HttpResponse("OK")
def data_aquaponics_WaterTemp(request):
    if request.method=='POST' :
        id=request.POST['id']
        data=request.POST['data']
        date=request.POST['date']
        type=request.POST['type']
        print("data   ", data, sep=" : --****- :")
        print("date ", date, sep=": -****-- :")
        print("id ", id, sep=": --**- :")
        print("type ", type, sep=": --**- :")
        json_data=(id,data,date,type)
        conn = create_connection()
        with conn:
            store_data(conn,json_data)
    return HttpResponse("OK")
def data_aquaponics_pH(request):
    if request.method=='POST' :
        id=request.POST['id']
        data=request.POST['data']
        date=request.POST['date']
        type=request.POST['type']
        print("data   ", data, sep=" : --****- :")
        print("date ", date, sep=": -****-- :")
        print("id ", id, sep=": --**- :")
        print("type ", type, sep=": --**- :")
        json_data=(id,data,date,type)
        conn = create_connection()
        with conn:
            store_data(conn,json_data)
    return HttpResponse("OK")            

def get_data_aquaponics_Humidity(request):
    res = {}
    if request.is_ajax():
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM data_aquaponics WHERE type = 'Humidity'")
            rows = cur.fetchall()
            for row in rows :
                print(row)
            res['data']=rows[-1][1]
            res['id']=rows[-1][0]
    return JsonResponse(res)
def get_last_date(request):
    if request.is_ajax():
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM data_aquaponics WHERE type = 'Humidity'")
            rows = cur.fetchall()
            row=rows[-1][2]
    return HttpResponse(row)    
def get_data_aquaponics_Temperature(request):
    res = {}
    if request.is_ajax():
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM data_aquaponics WHERE type = 'Temperature'")
            rows = cur.fetchall()
            for row in rows :
                print(row)
            res['data']=rows[-1][1]
            res['id']=rows[-1][0]
    return JsonResponse(res)         
def get_data_aquaponics_WaterTemp(request):
    res = {}
    if request.is_ajax():
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM data_aquaponics WHERE type = 'WaterTemp'")
            rows = cur.fetchall()
            for row in rows :
                print(row)
            res['data']=rows[-1][1]
            res['id']=rows[-1][0]
    return JsonResponse(res)     
def get_data_aquaponics_pH(request):
    res = {}
    if request.is_ajax():
        conn = create_connection()
        with conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM data_aquaponics WHERE type = 'pH'")
            rows = cur.fetchall()
            for row in rows :
                print(row)
            res['data']=rows[-1][1]
            res['id']=rows[-1][0]
    return JsonResponse(res)    
def get_data_aquaponics_Humidity_Date(date):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT data FROM data_aquaponics WHERE type = 'Humidity' and date=?", (date,))
        rows = cur.fetchall()
        if not rows:
            row=None
        else :
            if(len(rows)==1):
                row=rows[0]
            else :
                row=rows[-1]
    return row
def get_data_aquaponics_Temperature_Date(date):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT data FROM data_aquaponics WHERE type = 'Temperature' and date=?", (date,))
        rows = cur.fetchall()
        if not rows:
            row=None
        else :
            if(len(rows)==1):
                row=rows[0]
            else :
                row=rows[-1]
    return row
def get_data_aquaponics_WaterTemp_Date(date):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT data FROM data_aquaponics WHERE type = 'WaterTemp' and date=?", (date,))
        rows = cur.fetchall()
        if not rows:
            row=None
        else :
            if(len(rows)==1):
                row=rows[0]
            else :
                row=rows[-1]
    return row
def get_data_aquaponics_pH_Date(date):
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT data FROM data_aquaponics WHERE type = 'pH' and date=?", (date,))
        rows = cur.fetchall()
        if not rows:
            row=None
        else :
            if(len(rows)==1):
                row=rows[0]
            else :
                row=rows[-1]
    return row

def read(request):
    if request.is_ajax():
        Time=request.GET['date']
        print("DATE :  ", Time, sep=" : --- :")
        Hdata=get_data_aquaponics_Humidity_Date(Time)
        Tdata=get_data_aquaponics_Temperature_Date(Time)
        Wdata=get_data_aquaponics_WaterTemp_Date(Time)
        Pdata=get_data_aquaponics_pH_Date(Time)
        if(Hdata is None or Tdata is None or Pdata is None or Wdata is None):
            data = {}
            return JsonResponse(data)
        else :
            SHdata=str(Hdata).replace("('", "").replace("',)", "")
            STdata=str(Tdata).replace("('", "").replace("',)", "")
            SWdata=str(Wdata).replace("('", "").replace("',)", "")
            SPdata=str(Pdata).replace("('", "").replace("',)", "")
            print("get_data_aquaponics_Humidity_Date ", Hdata, sep=" : --- :")
            print("get_data_aquaponics_Temperature_Date ", Tdata, sep=": --- :")
            print("get_data_aquaponics_WaterTemp_Date ", Wdata, sep=": --- :")
            print("get_data_aquaponics_pH_Date ", Pdata, sep=": --- :")
            print("SHdata ", SHdata, sep=" : --- :")
            print("STdata ", STdata, sep=": --- :")
            print("SWdata ", SWdata, sep=": --- :")
            print("SPdata ", SPdata, sep=": --- :")
            json_data1 = json.loads(SHdata)
            json_data2 = json.loads(STdata)
            json_data3 = json.loads(SWdata)
            json_data4 = json.loads(SPdata)
            print("json_data1 ", json_data1[0]['y'], sep=" : --- :")
            print("json_data2 ", json_data2, sep=": --- :")
            print("json_data3 ", json_data3, sep=": --- :")
            print("json_data4 ", json_data4, sep=": --- :")
            
            temp = [float(line['y']) for line in json_data1]
            humy = [float(line['y']) for line in json_data2]
            Water = [float(line['y']) for line in json_data3]
            ph = [float(line['y']) for line in json_data4]
            x0 = [datetime.fromtimestamp(int(line['x']) / 1e3) for line in json_data1]
            x1 = [datetime.fromtimestamp(int(line['x']) / 1e3) for line in json_data2]
            x2 = [datetime.fromtimestamp(int(line['x']) / 1e3) for line in json_data3]
            x3 = [datetime.fromtimestamp(int(line['x']) / 1e3) for line in json_data4]
            print("temp ", temp, sep=" : --- :")
            print("humy ", humy, sep=": --- :")
            print("Water ", Water, sep=": --- :")
            print("ph ", ph, sep=": --- :")
            print("x0 ", x0, sep=" : --- :")
            print("x1 ", x1, sep=": --- :")
            print("x2 ", x2, sep=": --- :")
            print("x3 ", x3, sep=": --- :")
            random_x0 = [ line.strftime("%H:%M:%S") for line in x0 ]
            random_x1 = [ line.strftime("%H:%M:%S") for line in x1 ]
            random_x2 = [ line.strftime("%H:%M:%S") for line in x2 ]
            random_x3 = [ line.strftime("%H:%M:%S") for line in x3 ]
            random_y0 = temp
            random_y1 = humy
            random_y2 = Water
            random_y3 = ph
            

            trace0 = go.Scatter(
            x = random_x0,
            y = random_y0,
            mode = 'lines',
            name = 'Temp(°C)'
            
            )

            trace1 = go.Scatter(
            x = random_x1,
            y = random_y1,
            mode = 'lines',
            name = 'Humidity(%)'
            
            )

            trace2 = go.Scatter(
            x = random_x2,
            y = random_y2,
            mode = 'lines',
            name = 'WaterTemp(°C)'
            )

            trace3 = go.Scatter(
            x = random_x3,
            y = random_y3,
            mode = 'lines',
            name = 'pH'
            )
            # Structure traces as datasets
            data1 = [trace0]
            data2 = [trace1]
            data3 = [trace2]
            data4 = [trace3]

        # Build figures
            fig1 = go.Figure(data=data1)
            fig2 = go.Figure(data=data2)
            fig3 = go.Figure(data=data3)
            fig4 = go.Figure(data=data4)
            figs = cf.subplots([fig1, fig2, fig3, fig4],shape=(2,2))
            figs['layout'].update(height=630, width=1250,
                            title='Data For Aquaponics')
            div = opy.plot(figs, auto_open=True, output_type='div')
            data = {
                                'my_data':div
                        }
        return JsonResponse(data)

        
def getname(request, template_name='settings.html'):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        itemValue = form['temp'].value()
        from firebase import firebase
        aa = firebase.FirebaseApplication(
                        '********************************', None)
        Result = aa.put('/temp/', 'data', itemValue)
        #Result = aa.put('/temp/', 'data')

        print(Result)
        return render(request, template_name)
