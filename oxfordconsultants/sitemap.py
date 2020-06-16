from django.contrib import sitemaps
from django.contrib.sites.models import Site
from django.urls import reverse

from frontend.views import services_list


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.6
    changefreq = 'weekly'
    protocol = 'https'

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='www.oxfordconsultantsgh.com', name='www.oxfordconsultantsgh.com')
        return super(StaticViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        _items = [reverse('frontend:home'), reverse('frontend:about'), reverse('frontend:contact'),
                  reverse('frontend:testimonials')]
        for service in services_list:
            _items.append(reverse('frontend:services', args=(service.get('slug'),)))
        return _items

    def location(self, item):
        return item
