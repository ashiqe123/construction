from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path("log",views.log,name='log'),
    path('sig',views.sig,name='sig'),
    path('services',views.services,name='services'),
    path('meterial',views.meterial,name='meterial'),
    path('dt',views.dt,name='dt'),
    path('home',views.home,name='home'),
    path('lgout',views.lgout,name='lgout'),
    path('about',views.about,name='about')
]