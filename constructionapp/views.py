from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")
    
def log(request):
    return render(request,"login.html")

def sig(request):
    return render(request,"signin.html")

def services(request):
    return render(request,"services.html")

def meterial(request):
    return render(request,"meterials.html")

def dt(request):
    return render(request,'dt.html')

def home(request):
    return render(request,'home.html')

def lgout(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")