from django.contrib import admin

# Register your models here.
from frontend.models import Insight, Testimonial, Question, PossibleAnswer, Vote, PersonToken


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


def reset_questions(modeladmin, request, queryset):
    queryset.update(voting_stopped=False, next_resolution_launched=False)
    Vote.objects.all().delete()


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    actions = [
        reset_questions
    ]


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass


@admin.register(PossibleAnswer)
class PossibleAnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonToken)
class PersonTokenAdmin(admin.ModelAdmin):
    pass