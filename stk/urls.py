from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pay/',views.pay,name='pay'),
    path('stk/',views.stk,name='stk'),
]
