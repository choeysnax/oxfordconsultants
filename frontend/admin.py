from django.contrib import admin

# Register your models here.
from frontend.models import Insight, Testimonial, Question, PossibleAnswer, Vote, PersonToken


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass


@admin.register(PossibleAnswer)
class PossibleAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonToken)
class PersonTokenAdmin(admin.ModelAdmin):
    pass