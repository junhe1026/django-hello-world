from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('问题',               {'fields': ['question_text']}),
        ('发布时间',            {'fields': ['pub_date'], 'classes': ['']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_per_page = 20


admin.site.register(Question, QuestionAdmin)
