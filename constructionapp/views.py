from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")
    
def log(request):
    return render(request,"login.html")

def sig(request):
    return render(request,"signin.html")