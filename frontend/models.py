from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable

from .blocks import BaseStreamBlock


class HomePage(Page):
    pass


class Insight(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    tag = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    author = models.CharField(max_length=140)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


class Section(Orderable):
    title = models.CharField(max_length=140, blank=True)
    body = RichTextField(null=True, blank=True)
    page = ParentalKey('RegistrationPage', on_delete=models.CASCADE, related_name='sections')
    file = models.FileField(upload_to='files/', null=True, blank=True)
    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        FieldPanel('file'),
    ]


class RegistrationPage(Page, ClusterableModel):
    introduction_text = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('introduction_text'),
            InlinePanel('sections', label="Section"),

        ], heading="Sections")
    ]


class StandardPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
