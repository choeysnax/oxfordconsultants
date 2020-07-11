from django.urls import path, include

from frontend import views

app_name = 'frontend'
urlspatterns_remains = [
    path('', views.index_view, name='home'),
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('testimonials', views.testimonials_view, name='testimonials'),
    path('contact', views.contact_view, name='contact'),
    path('services/<slug:slug>', views.services_view, name='services'),
    path('upload-form', views.upload_form_view, name='upload_form'),
]
urlpatterns = [

    path('', views.redirect_to_english),
    # path('fr/', include(urlspatterns_remains)),
    path('en/', include(urlspatterns_remains)),

]
