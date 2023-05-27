from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import VehicleSerializers
from paynrentapp.models import Vehicle
from . import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleInterface(request):
    return render(request,"VehicleInterface.html")

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleSubmit(request):
    if request.method == 'POST':
        vehicle_serializers = VehicleSerializers(data=request.data)
        if vehicle_serializers.is_valid():
            vehicle_serializers.save()
            return render(request,"VehicleInterface.html",{'message':"Record Submitted Sucessfully"})
        return render(request,"VehicleInterface.html",{'message':"Fail to Submit Record"})
    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleDisplay(request):
    try:
        if request.method == 'GET':
            q = "select V.*, (select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicle V"
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            return render(request,"VehicleDisplay.html",{'data':records})
    except Exception as e:
        print("Error : " ,e)
        return render(request,"VehicleDisplay.html",{'data':{}})  

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def VehicleDisplayById(request):
    try:
        if request.method == 'GET':
            q = "select V.*, (select C.categoryname from paynrentapp_category C where C.id=V.categoryid) as categoryname, (select S.subcategoryname from paynrentapp_subcategory S where S.id=V.subcategoryid) as subcategoryname from paynrentapp_vehicle V where V.id={0}".format(request.GET['id'])
            print(q)
            cursor = connection.cursor()
            cursor.execute(q)
            record = tuple_to_dict.ParseDictSingleRecord(cursor)
            print("xxxxxxxxxx",record)
            return render(request,"VehicleDisplayById.html",{'data':record})
    except Exception as e:
        print("Error : ",e)
        return render(request,"VehicleDisplayById.html",{'data':record})

@xframe_options_exempt    
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

@xframe_options_exempt        
@api_view(['GET','POST','DELETE'])
def DisplayVehicleIcon(request):
    try :
        if request.method == 'GET':
            return render(request,"VehicleDisplayIcon.html",{'data':request.GET})
    except Exception as e:
        print("Error : ",e)
        return render(request,"VehicleDisplayIcon.html",{'data':[]})

@xframe_options_exempt    
@api_view(['GET','POST','DELETE'])
def SaveVehicleIcon(request):
    try :
        if request.method == 'POST':
            vehicle = Vehicle.objects.get(pk=request.POST['id'])
            vehicle.icon = request.FILES['icon']
            vehicle.save()
            return redirect('/api/display_vehicle')
    except Exception as e:
        print("Error : ",e)
        return redirect('/api/display_vehicle')