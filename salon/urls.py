from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('szolgaltatasok/', views.services_view, name='services'),
    path('idopontfoglalas/', views.booking_view, name='booking'),
    path('api/booked-slots/', views.booked_slots_api, name='booked_slots_api'),
    path('rolunk/', views.about_view, name='about'),
    path('kapcsolat/', views.contact_view, name='contact'),
]