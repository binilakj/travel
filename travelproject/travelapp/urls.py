from . import views
from django.urls import path

urlpatterns = [
    path('', views.app, name='app')
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('details/', views.details, name='details'),
#     path('thanks/', views.thanks, name='thanks')
]
