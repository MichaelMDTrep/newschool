from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, CourseCategory, CourseCompleted, CourseLink
import os
from django.utils import timezone
from django.contrib import messages
import urllib


@login_required
def curriculum(request):

    courses = Course.objects.all()
    categories = CourseCategory.objects.all()

    context = {
        'page': 'curriculum',
        'courses': courses,
        'categories': categories,
        'title': 'Curriculum',
    }

    return render(request, 'curriculum/curriculum.html', context)


@login_required
def course(request, course_id):

    course = get_object_or_404(Course, pk=course_id)
    course_links = CourseLink.objects.filter(course=course)
    tiny_mce_key = os.environ.get("TINY_MCE_KEY")

    if request.method == "POST":
        course_complete = CourseCompleted(user=request.user, course=course, date=timezone.now())
        course_complete.save()
        messages.success(request, f'{course.title} marked complete for today!')
        return redirect('curriculum')
    
    context = {
        'page': 'curriculum',
        'course': course,
        'course_links': course_links,
        'tiny_mce_key': tiny_mce_key,
        'title': f'{course.title}',
    }

    return render(request, 'curriculum/course.html', context)


@login_required
def add_course_link(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    if request.user.is_superuser:

        def decode(raw_text):
            return urllib.parse.unquote(raw_text, encoding='utf-8', errors='replace').replace("+", " ")

        if request.method == "POST":
            data = request.body.decode().split("=")
            name = decode(data[2].split('&')[0])
            link = decode(data[3].split('&')[0])

            course_link = CourseLink(name=name, link=link, course=course)
            course_link.save()
                
            messages.success(request, 'Link added!')
            return redirect('course', course_id)

        context = {
            'page': 'curriculum',
            'course': course,
            'title': 'Add Course Link',
        }

        return render(request, 'curriculum/add_course_link.html', context)
    
    else:
        messages.warning(request, 'You are not authorized to add course links.')
        return redirect('home')
    

@login_required
def delete_course(request, course_id):

    course = get_object_or_404(Course, pk=course_id)

    if request.user.is_superuser:

        if request.method == "POST":
            course.delete()
            messages.success(request, 'Course successfully deleted!')
            return redirect('curriculum')

        context = {
            'page': 'curriculum',
            'course': course,
            'title': 'Delete Course',
        }

        return render(request, 'curriculum/delete_course.html', context)
    
    else:
        messages.warning(request, 'You are not authorized to manage courses.')
        return redirect('home')
    

@login_required
def edit_course(request, course_id):

    course = get_object_or_404(Course, pk=course_id)
    course_categories = CourseCategory.objects.all()

    if request.user.is_superuser:

        def decode(raw_text):
            return urllib.parse.unquote(raw_text, encoding='utf-8', errors='replace').replace("+", " ")

        if request.method == "POST":
            data = request.body.decode().split("=")
            title = decode(data[2].split('&')[0])
            content = decode(data[3].split('&')[0])
            category = decode(data[4].split('&')[0])

            course.title = title
            course.content = content
            course.category = get_object_or_404(CourseCategory, pk=category)
            course.save()
                
            messages.success(request, 'Course successfully edited!')
            return redirect('course', course_id)
        
        context = {
            'page': 'curriculum',
            'course': course,
            'course_categories': course_categories,
            'title': 'Edit Course',
        }

        return render(request, 'curriculum/edit_course.html', context)
    
    else:
        messages.warning(request, 'You are not authorized to manage courses.')
        return redirect('home')