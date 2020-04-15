from django.db import models


# Create your models here.


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
