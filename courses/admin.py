from django.contrib import admin
from .models import Course, Chapter
from .models import  Quiz, Question, Answer
from django import forms  # Import forms module here

class AnswerInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_correct_answer = False
        for form in self.forms:
            if form.cleaned_data.get('is_correct'):
                has_correct_answer = True
                break
        if not has_correct_answer:
            raise forms.ValidationError('At least one answer must be marked as correct.')

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    formset = AnswerInlineFormset

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    inlines = [AnswerInline]





class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]
    list_display = ['title', 'description', 'image_display']

    def image_display(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url)
        return '-'
    image_display.allow_tags = True
    image_display.short_description = 'Image'

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image')
        }),
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Quiz)

admin.site.register(Question, QuestionAdmin)
