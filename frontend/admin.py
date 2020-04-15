from django.contrib import admin

# Register your models here.
from frontend.models import Insight


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    pass
