from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import AdministratorSerializers
from paynrentapp.models import Administrator
from . import tuple_to_dict

@api_view(['GET','POST','DELETE'])
def AdminLogin(request):
    return render(request,"AdminLogin.html", {'message':''})

@api_view(['GET','POST','DELETE'])
def CheckAdminLogin(request):
    try:
        if request.method == 'GET':
            q = "select * from paynrentapp_administrator where (mobileno='{0}' or emailid='{0}') and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("Check", record)           
            if(len(record)==0):
                return render(request,"AdminLogin.html",{'message':"Invalid AdminId/Password"})
            else:
                return render(request,"DashBoard.html", {'data':record[0]})
    except Exception as e:
        print("Error : ",e)
        return render(request,"DashBoard.html",{'data':[]})
    
@api_view(['GET','POST','DELETE'])
def VehicleEdit(request):
    try :
        if request.method == 'GET' :
            if request.GET['btn'] == 'Edit' :
                vehicle = Vehicle.objects.get(pk=request.GET['id'])
                vehicle.categoryid = request.GET['categoryid']
                vehicle.subcategoryid = request.GET['subcategoryid']
                vehicle.model_year = request.GET['model_year']
                vehicle.variant = request.GET['variant']
                vehicle.price = request.GET['price']
                vehicle.insured = request.GET['insured']
                vehicle.registration_no = request.GET['registration_no']
                vehicle.owner_name = request.GET['owner_name']
                vehicle.mobile_no = request.GET['mobile_no']
                vehicle.color = request.GET['color']
                vehicle.fuel_type = request.GET['fuel_type']
                vehicle.no_of_seats = request.GET['no_of_seats']
                vehicle.transmission_type = request.GET['transmission_type']
                vehicle.save()
            else :
                vehicle = Vehicle.objects.get(pk=request.GET['id'])
                vehicle.delete()
            return redirect('/api/display_vehicle')
    except Exception as e:
        print("Error :" ,e)
        return redirect('/api/display_vehicle')
    
