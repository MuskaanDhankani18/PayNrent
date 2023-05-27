"""djpaynrentapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,re_path
from paynrentapp import Category_view
from paynrentapp import SubCategory_view
from paynrentapp import Vehicle_view
from paynrentapp import Admin_Login
from paynrentapp import user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/categoryinterface',Category_view.CategoryInterface),
    re_path(r'^api/categorysubmit',Category_view.CategorySubmit),
    re_path(r'^api/displaycategory',Category_view.DisplayCategory),
    re_path(r'^api/display_category_by_id',Category_view.DisplayByCategoryId),
    re_path(r'^api/category_edit',Category_view.EditCategory),
    re_path(r'^api/display_category_icon/$',Category_view.DisplayCategoryIcon),
    re_path(r'^api/category_save_icon',Category_view.CategorySaveIcon),
    re_path(r'^api/jsondisplaycategory',Category_view.DisplayCategoryJSON),
    
    re_path(r'^api/subcategory_interface',SubCategory_view.SubCategoryInterface),
    re_path(r'^api/subcategory_submit',SubCategory_view.SubCategorySubmit),
    re_path(r'^api/subcategory_display',SubCategory_view.SubCategoryDisplay),
    re_path(r'^api/displaysubcategorybyid',SubCategory_view.DisplaySubCategoryById),
    re_path(r'^api/edit_subcategory',SubCategory_view.EditSubCategory),
    re_path(r'^api/display_subcategory_icon',SubCategory_view.DisplaySubCategoryIcon),
    re_path(r'^api/save_subcategory_icon',SubCategory_view.SubCategorySaveIcon),
    re_path(r'^api/jsondisplaysubcategory',SubCategory_view.DisplaySubCategoryJSON),

    re_path(r'^api/vehicle_interface',Vehicle_view.VehicleInterface),
    re_path(r'^api/vehicle_submit',Vehicle_view.VehicleSubmit),
    re_path(r'^api/display_vehicle',Vehicle_view.VehicleDisplay),
    re_path(r'^api/vehicle_display_by_id',Vehicle_view.VehicleDisplayById),
    re_path(r'^api/edit_vehicle',Vehicle_view.VehicleEdit),
    re_path(r'^api/vehicledisplayicon',Vehicle_view.DisplayVehicleIcon),
    re_path(r'^api/save_vehicle_icon',Vehicle_view.SaveVehicleIcon),

    re_path(r'^api/adminlogin',Admin_Login.AdminLogin),
    re_path(r'^api/checkadminlogin',Admin_Login.CheckAdminLogin),
    re_path(r'^api/index',user_view.Index),
    re_path(r'^api/displayvehicleforuser',user_view.VehicleDisplayForUser),
    re_path(r'^api/uservehiclelist',user_view.PageUserVehicleList),
    re_path(r'^api/displayselectedvehicle',user_view.DisplaySelectedVehicle),
    re_path(r'^api/showvehiclelist',user_view.ShowVehicleList),
    re_path(r'^api/setmobileandemail',user_view.SetMobileAndEmail),
]   
