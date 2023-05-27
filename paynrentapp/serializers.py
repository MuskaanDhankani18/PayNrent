from rest_framework import serializers
from paynrentapp.models import Category
from paynrentapp.models import SubCategory
from paynrentapp.models import Vehicle
from paynrentapp.models import Administrator
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category    #model,fields are pre-defined keywords
        fields = ('id','categoryname','description','icon')

class SubCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory    
        fields = ('id','categoryid','brandname','subcategoryname','description','icon')    

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id','categoryid','subcategoryid','model_year','variant','price','insured','registration_no','owner_name','mobile_no','color','fuel_type','no_of_seats','transmission_type','icon')        

class AdministratorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','adminname','mobileno','emailid','password')
