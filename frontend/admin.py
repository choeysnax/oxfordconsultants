from django.contrib import admin

# Register your models here.
from frontend.models import Insight, Testimonial


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass
