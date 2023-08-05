from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Manage
from django.contrib.auth import logout
from django.contrib import messages
import barcode
from barcode.writer import ImageWriter
import random
# Create your views here.
def index(request):
    return render(request,"manage/index.html")

def handlelogin(request):
    return render(request,"manage/login.html")
def generate_random_12_digit_number():
    random_number = random.randint(10**11, 10**12 - 1)
    random_number_str = str(random_number)
    if len(random_number_str) < 12:
        random_number_str = random_number_str.zfill(12)
    return random_number_str

def count():
    random_number = random.randint(100, 999)
    return random_number
def barcodeGenerate(request,manage_id):
    random_12_digit_number = generate_random_12_digit_number()
    ean = barcode.get('ean13', random_12_digit_number, writer=ImageWriter())
    counter_value = count()
    filename = f'static/assets/barcodeImage/ean{counter_value}'
    ean.save(filename)
    filename
    u'ean15.png'
    return redirect("/manage/home/")

def signup(request):
    return render(request,"manage/signup.html")

def handlelogout(request):
    # return render(request,"manage/index.html")
    logout(request)
    messages.info(request,"Logout Success")
    return redirect("/")

def malkhana_home(request):
    manage = Manage.objects.all()
    # return HttpResponse("manageloyee home page")
    # return render (request, "login.html",{'manage': manage})
    return render(request,"manage/home.html",{'manage':manage})

def about(request):
    return render(request,"manage/about.html")

def add_details(request):
    if request.method == "POST":
        #  data fetch
        FIR_Number = request.POST.get("FIR_Number")
        Item_Name = request.POST.get("Item_Name")
        IPC_Section = request.POST.get("IPC_Section")
        Crime_scene = request.POST.get("Crime_scene")
        Crime_date = request.POST.get("Crime_date")
        Crime_time = request.POST.get("Crime_time")
        Crime_witnesses = request.POST.get("Crime_witnesses")
        Crime_inspector = request.POST.get("Crime_inspector")
        Item_status = request.POST.get("Item_status")
        where_its_kept = request.POST.get("where_its_kept")
        # At_what_time = request.POST.get("At_what_time")
   
       

        #create model object and set the data   
        m=Manage()
        m.FIR_Number = FIR_Number
        m.Item_Name = Item_Name
        m.IPC_Section = IPC_Section
        m.Crime_scene = Crime_scene
        m.Crime_date = Crime_date
        m.Crime_time= Crime_time
        m.Crime_witnesses = Crime_witnesses
        m.Crime_inspector = Crime_inspector
        m.where_its_kept = where_its_kept
        
        if Item_status is None:
            m.working = False
        else:
            m.working = True
        #save the object
        m.save()    
        print("HELlO3")

        #prepare message


        return redirect("/manage/home/")
    return render(request, "manage/add_details.html", {}) 

def delete_details(request,manage_id):
    manage = Manage.objects.get(pk = manage_id)
    manage.delete()
    return redirect("/manage/home/")

def update_details(request,manage_id):
    manage = Manage.objects.get(pk = manage_id)
    return render(request,"manage/update_details.html",{'manage':manage})

def do_update_details(request, manage_id):
    # Get the Manage object with the given manage_id
    try:
        manage = Manage.objects.get(pk=manage_id)
    except Manage.DoesNotExist:
        # Handle the case when the Manage object doesn't exist
        return HttpResponse("Manage object not found", status=404)

    if request.method == "POST":
        # Data fetch from the POST request
        FIR_Number = request.POST.get("FIR_Number")
        Item_Name = request.POST.get("Item_Name")
        IPC_Section = request.POST.get("IPC_Section")
        Crime_scene = request.POST.get("Crime_scene")
        Crime_date = request.POST.get("Crime_date")
        Crime_time = request.POST.get("Crime_time")
        Crime_witnesses = request.POST.get("Crime_witnesses")
        Crime_inspector = request.POST.get("Crime_inspector")
        Item_status = request.POST.get("Item_status")
        where_its_kept = request.POST.get("where_its_kept")

        # Update the attributes of the Manage object with the new data
        manage.FIR_Number = FIR_Number
        manage.Item_Name = Item_Name
        manage.IPC_Section = IPC_Section
        manage.Crime_scene = Crime_scene
        manage.Crime_date = Crime_date
        manage.Crime_time = Crime_time
        manage.Crime_witnesses = Crime_witnesses
        manage.Crime_inspector = Crime_inspector
        manage.where_its_kept = where_its_kept
        
        if Item_status is None:
            manage.working = False
        else:
            manage.working = True

        # Save the updated Manage object
        manage.save()

        return redirect("/manage/home/")

    # If it's not a POST request, render the template with the Manage object data
    return render(request, "manage/home.html", {"manage": manage})