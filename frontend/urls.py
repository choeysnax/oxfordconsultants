from django.urls import path

from frontend import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.index, name='about'),
    path('contact', views.index, name='contact'),

]
