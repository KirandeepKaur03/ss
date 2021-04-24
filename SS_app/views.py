from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from SS_app.models import Queries,adminlist
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about_us.html') 

def power(request):
    return render(request,'power.html') 

def voltage(request):
    return render(request,'voltage.html')

def solar(request):
    return render(request,'solar.html')

def evehicle(request):
    return render(request,'evehicle.html')               

def shop(request):
    return render(request,'shop.html') 

def sel_power(request):
    return render(request,'sel_power.html')     

def sel_voltage(request):
    return render(request,'sel_voltage.html')

def sel_solar(request):
    return render(request,'sel_solar.html')

def sel_evehicle(request):
    return render(request,'sel_evehicle.html')            

def bl_1(request):
    return render(request,'bl_1.html')    

def bl_2(request):
    return render(request,'bl_2.html')

def bl_3(request):
    return render(request,'bl_3.html')    

def bl_4(request):
    return render(request,'bl_4.html')

def bl_5(request):
    return render(request,'bl_5.html')    

def bl_6(request):
    return render(request,'bl_6.html')   


@csrf_exempt
def add_queries(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        Q = Queries(name=name, email=email,mobile=mobile,message=message)
        Q.save()
        messages.success(request, 'Query saved successfully. We will revert back shortly.')
    return redirect('/')


@csrf_exempt
def admin_login(request):
    return render(request,'admin_login.html')   

@csrf_exempt
def admin_login1(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        if adminlist.objects.filter(adminid__icontains=Username).exists():
            data = adminlist.objects.get(adminid__icontains=Username)  
            print(data.password) 
            print(password)
            print(data.adminid)
            if (password == data.password):
                user = data.adminid
                if user is not None:
                    return render(request,'admin_login1.html')
            else:
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('Invalid Username')
    else:
        return redirect('/')
       
def admin_logout(request):
    return redirect('/')

def queries(request):
    records = Queries.objects.all()
    return render(request, 'queries.html', {'data': records})  

@csrf_exempt
def query_delete(request, id):
    if Queries.objects.filter(id=id).exists():
        data = Queries.objects.get(id=id)
        data.delete()
        return redirect('/admin_login1/queries/')    

@csrf_exempt
def add_admin(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        if adminlist.objects.filter(adminid=Username).exists():
            messages.error(request, 'You are already an admin.')
            return render(request, 'add_admin.html')
        else:
            data = adminlist(adminid=Username,
                            password=password)
            data.save()
            messages.success(request, 'Admin created successfully')
            return render(request, 'add_admin.html')
    return render(request, 'add_admin.html')        