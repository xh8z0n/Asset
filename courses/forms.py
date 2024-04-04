from django import forms
from .models import Course, Chapter

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title', 'content_type', 'content']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
