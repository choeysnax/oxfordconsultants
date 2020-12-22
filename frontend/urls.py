from django.urls import path, include

from frontend import views

app_name = 'frontend'
urlspatterns_remains = [
    path('', views.index_view, name='home'),
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('voting/', views.voting_index, name='voting_index'),
    path('voting/summary/', views.voting_view_summary, name='voting_view_summary'),
    path('voting/<int:ordering>/', views.voting_view, name='voting_view'),
    path('voting/<int:ordering>/answer/', views.voting_view_answer, name='voting_view_answer'),
    path('voting/<int:ordering>/results/', views.voting_view_results, name='voting_view_results'),
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
