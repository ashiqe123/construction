from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path("log",views.log,name='log'),
    path('sig',views.sig,name='sig'),
]