from django.contrib import admin
from django.urls import path
from .views import* 


urlpatterns = [
    path("home/",malkhana_home),
    path("add-details/",add_details),
    path("delete-details/<int:manage_id>",delete_details),
    path("update-details/<int:manage_id>",update_details),
    path("do-update-details/<int:manage_id>",do_update_details),
    path("barcodeGenerate/<int:manage_id>",barcodeGenerate),
    path("about/",about),
    path("index/",index),
    path("login/",handlelogin),
    path("signup/",signup),
    path("logout/",handlelogout),
    path('admin/', admin.site.urls),

    
]