from django.urls import path

from frontend import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index_view, name='home'),
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('services/<slug:slug>', views.services_view, name='services'),

]
