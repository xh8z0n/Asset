from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from .models import Course, Chapter
from .forms import CourseForm, ChapterForm
from django.shortcuts import  get_object_or_404
from django.views.generic import ListView







def courses_page(request):
    courses = Course.objects.all()  # Retrieve all courses from the database
    return render(request, 'courses.html', {'courses': courses})



from django.http import HttpResponseNotFound, FileResponse
from .models import Chapter

@login_required

def chapter_file_view(request, filename):
    try:
        chapter = Chapter.objects.get(content=filename)
    except Chapter.DoesNotExist:
        return HttpResponseNotFound("File not found")

    file_path = chapter.content.path
    return FileResponse(open(file_path, 'rb'))

import base64


@login_required
def course_detail(request, course_title):
    course = get_object_or_404(Course, title=course_title.replace('-', ' '))
    chapters = Chapter.objects.filter(course=course)

    for chapter in chapters:
        if chapter.content_type == 'PDF':
            with open(chapter.content.path, 'rb') as f:
                pdf_data = f.read()
                chapter.base64_pdf = base64.b64encode(pdf_data).decode('utf-8')


    return render(request, 'courses/course_detail.html', {'course': course, 'chapters': chapters})







def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

def create_chapter(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.course = course
            chapter.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = ChapterForm()
    return render(request, 'courses/create_chapter.html', {'form': form, 'course': course})
