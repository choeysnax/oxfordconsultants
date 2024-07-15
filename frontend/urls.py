from django.urls import path, include
from django_distill import distill_path

from frontend import views
from frontend.types import UrlMap
from frontend.views import get_services_list

app_name = 'frontend'


urls_maps: list[UrlMap] = [{
    'url': '',
    'view': views.index_view,
    'name': 'index',
    'distill_file': 'index.html',
}, {
    'url': '',
    'view': views.index_view,
    'name': 'home',
    'distill_file': 'home.html',
}, {
    'url': 'about',
    'view': views.about_view,
    'name': 'about',
    'distill_file': 'about.html'
}, {
    'url': 'testimonials',
    'view': views.testimonials_view,
    'name': 'testimonials',
    'distill_file': 'testimonials.html'
}, {
    'url': 'contact',
    'view': views.contact_view,
    'name': 'contact',
    'distill_file': 'contact.html'
}, {
    'url': 'services/<slug:slug>',
    'view': views.services_view,
    'name': 'services',
    'distill_file': 'services/{}.html',
    'distill_func': get_services_list,
}]

static_page_urlpatterns = []

for url_map in urls_maps:
    static_page_urlpatterns.append(path(url_map['url'], url_map['view'], name=url_map['name']))
    distill_path_kwargs = {
        'name': url_map['name'],
    }
    if url_map.get('distill_file'):
        distill_path_kwargs['distill_file'] = url_map['distill_file']
    if url_map.get('distill_func'):
        distill_path_kwargs['distill_func'] = url_map['distill_func']

    static_page_urlpatterns.append(
        distill_path(
            url_map['url'],
            url_map['view'],
            **distill_path_kwargs,
        )
    )

voting_urlpatterns = [
    path('voting/', views.voting_index, name='voting_index'),
    path('voting/summary/', views.voting_view_summary, name='voting_view_summary'),
    path('voting/<int:ordering>/', views.voting_view, name='voting_view'),
    path('voting/<int:ordering>/launch/', views.voting_view_launch, name='voting_view_launch'),
    path('voting/<int:ordering>/answer/', views.voting_view_answer, name='voting_view_answer'),
    path('voting/<int:ordering>/results/', views.voting_view_results, name='voting_view_results'),
    path('voting/upload-form', views.upload_form_view, name='upload_form'),
]

urlpatterns = [
    path('', include(static_page_urlpatterns + voting_urlpatterns)),
]
