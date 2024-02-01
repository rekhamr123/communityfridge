from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('memberregistration/', views.memberregistration, name='memberregistration'),
    path('memberlogin/',views.memberlogin,name='memberlogin'),
    path('donations/', views.donations, name='donations'),
    path('item_request/', views.item_request, name='item_request'),
    path('requests/', views.requests, name='requests'),
    path('login/donated_items/',views.donatedlist,name='donated_items'),
    path('login/',views.login,name='login'),
    path('login/admin/',views.admin,name='admin'),
    path('logout/',views.logout,name='logout'),
    path('login/requested_items/',views.requestedlist,name='requested_items'),
]
