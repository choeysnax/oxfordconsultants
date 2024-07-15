from django import forms
from django.db import models


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


class PersonToken(models.Model):
    token = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    weight = models.IntegerField(default=0)
    is_chairman = models.BooleanField(default=False)
    questions_to_skip = models.ManyToManyField('Question', blank=True)

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
    consensus = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    stats = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.slug}. {self.text}"


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE)
    person = models.ForeignKey(PersonToken, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.name} voted [{self.answer}] on [{self.question}]"