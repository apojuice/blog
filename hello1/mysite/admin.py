from django.contrib import admin
from .models import Question,Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QestionAdmin(admin.ModelAdmin):
    list_display = ['question_text','pub_date',]
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Title', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QestionAdmin)


# admin.site.register(Question)
admin.site.register(Choice)