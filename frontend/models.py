from django import forms
from django.contrib.postgres.fields import JSONField
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
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

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
    author = models.CharField(max_length=140, blank=True)
    company_name = models.CharField(max_length=140, blank=True)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


@register_snippet
class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    @property
    def file_name(self):
        return str(self.file.url.split('/uploads/')[1])


class UploadForm(forms.ModelForm):
    name = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        fields = ('file', 'name')
        model = Upload
        labels = {
            'file': ''
        }


class Section(Orderable):
    title = models.CharField(max_length=140, blank=True)
    body = RichTextField(null=True, blank=True)
    page = ParentalKey('RegistrationPage', on_delete=models.CASCADE, related_name='sections')
    file = models.FileField(upload_to='files/', null=True, blank=True)
    show_people = models.BooleanField(default=False)
    upload = models.BooleanField(default=False)
    upload_instruction_title = models.CharField(max_length=140, blank=True)
    upload_instruction_body = models.TextField(blank=True)
    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('body'),
            FieldPanel('file'),
        ], "Basics"),
        MultiFieldPanel([
            FieldPanel('upload'),
            FieldPanel('upload_instruction_title'),
            FieldPanel('upload_instruction_body'),
        ], "Upload section", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('show_people'),
        ], "People", classname="collapsible collapsed"),
    ]

    @property
    def people(self):
        return  self.person_set.all()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


@register_snippet
class Person(models.Model):
    name = models.CharField(max_length=140, blank=True)
    title = models.CharField(max_length=140, blank=True)
    description = RichTextField(null=True, blank=True)
    section = models.ManyToManyField(Section, blank=True)
    cv_url = models.URLField(blank=True)

    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('description'),
        FieldPanel('cv_url'),
        FieldPanel('section'),
        ImageChooserPanel('photo'),
    ]

    def __str__(self):
        return self.name


class RegistrationPage(Page, ClusterableModel):
    introduction_text = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('introduction_text'),
            InlinePanel('sections', label="Section"),

        ], heading="Sections")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['upload_form'] = UploadForm()
        return context


class StandardPage(Page):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class PersonToken(models.Model):
    token = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    weight = models.IntegerField(default=0)
    is_chairman = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PossibleAnswer(models.Model):
    ordering = models.IntegerField(default=0)
    text = models.CharField(max_length=100)
    consensus = models.TextField(blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('ordering', )


class Question(models.Model):
    ordering = models.IntegerField(default=0)
    text = models.TextField()
    voting_stopped = models.BooleanField(default=False)
    next_resolution_launched = models.BooleanField(default=False)
    slug = models.SlugField(null=True)
    possible_answers = models.ManyToManyField(PossibleAnswer)
    consensus = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE)
    stats = JSONField(default=dict)

    def __str__(self):
        return f"{self.slug}. {self.text}"


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE)
    person = models.ForeignKey(PersonToken, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.name} voted [{self.answer}] on [{self.question}]"