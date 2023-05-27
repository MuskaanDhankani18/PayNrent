from django.db import connection
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from paynrentapp.serializers import CategorySerializers
from paynrentapp.models import Category
from . import tuple_to_dict
import os
from django.views.decorators.clickjacking import xframe_options_exempt

# Create your views here.
@xframe_options_exempt
@api_view(['GET','POST'])
def CategoryInterface(request):
    return render(request,'CategoryInterface.html')

@xframe_options_exempt
@api_view(['GET','POST'])
def CategorySubmit(request):
    if request.method == 'POST':
        category_serializers = CategorySerializers(data=request.data)
        if category_serializers.is_valid():
            category_serializers.save()
            return render(request,"CategoryInterface.html",{"message":"Record Submitted Successfully !!"})
        return render(request,'CategoryInterface.html',{"message":"Fail to Submit Record"})

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayCategory(request):
    try:
        if request.method == 'GET':
            list_category = Category.objects.all()
            list_category_serializer = CategorySerializers(list_category,many=True)
            records=tuple_to_dict.ParseDict(list_category_serializer.data)
            print("xxxxx",records)
            return render(request,'CategoryDisplay.html',{'data':records})
    except Exception as e:
        print("Error : ",e)
        return render(request,'CategoryDisplay.html',{'data':{}})

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayByCategoryId(request):
    try:
        if request.method == 'GET':
            q="select * from paynrentapp_category where id={0}".format(request.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            return render(request,'DisplayById.html',{'data':record})
    except Exception as e:
        print("Error : ",e)
        return render(request,'DisplayById.html',{'data':{}})

@xframe_options_exempt
@api_view(['GET','POST'])
def EditCategory(request):
    try:
        if request.method == 'GET':
            if(request.GET['btn']=="EDIT"):
                category=Category.objects.get(pk=request.GET['id'])    #id here is hidden
                category.categoryname=request.GET['categoryname']
                category.description=request.GET['description']
                category.save()
                return redirect('/api/displaycategory')
            else:
                category=Category.objects.get(pk=request.GET['id'])
                category.delete()
                return redirect('/api/displaycategory')
    except Exception as e:
        print("Error : ",e)
        return redirect('/api/displaycategory')

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayCategoryIcon(request):
    try:
        if request.method == 'GET':
            return render(request,'Display_Category_Icon.html',{'data':dict(request.GET)}) 
    except Exception as e:
        print("Error : ",e)
        return render(request,'Display_Category_Icon.html',{'data':{}})

@xframe_options_exempt
@api_view(['GET','POST'])
def CategorySaveIcon(request):
    try:
        if request.method == 'POST':
                category=Category.objects.get(pk=request.POST['id'])    #id here is hidden
                category.icon="/static/" + request.FILES['icon'].name
                category.save()
                os.remove('E:/djpaynrentapp/djpaynrentapp/'+ request.POST['oldpic'])
                return redirect('/api/displaycategory')
    except Exception as e:
        print("Error : ",e)
        return redirect('/api/displaycategory')

@xframe_options_exempt
@api_view(['GET','POST'])
def DisplayCategoryJSON(request):
    try:
        if request.method == 'GET':
            list_category = Category.objects.all()
            list_category_serializer = CategorySerializers(list_category,many=True)
            records=tuple_to_dict.ParseDict(list_category_serializer.data)
            
            return JsonResponse(records, safe=False)
    except Exception as e:
        print("Error : ",e)
        return JsonResponse([], safe=False)