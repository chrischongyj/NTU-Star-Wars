from django.shortcuts import render
from .models import CourseInfo

def welcome(request):
    return render(request, './starwars/welcome.html', {'title': 'Welcome to End Star Wars'})


def havecourse(request):
    return render(request, './starwars/test.html')

def addcourse(request):
    course_name = request.POST["course_name"]
    course_code = request.POST["course_code"]
    course_au = request.POST["course_au"]

    course_info = CourseInfo(course_name=course_name, course_code=course_code, course_au=course_au)

    course_info.save()
    all_courses = CourseInfo.objects.all()

    return render(request, './starwars/want.html',  {'Courses': all_courses})

def selectcourse(request):
    course_name = request.POST["course_name"]
    course_code = request.POST["course_code"]
    course_au = request.POST["course_au"]

    my_obj = CourseInfo.objects.get(course_name=course_name, course_code=course_code, course_au=course_au)
    my_obj.delete()
    all_courses = CourseInfo.objects.all()

    return render(request, './starwars/want.html', {'Courses': all_courses})

def wantcourse(request):
    # course_name = request.POST["course_name"]
    # course_code = request.POST["course_code"]
    # course_au = request.POST["course_au"]

    # my_obj = CourseInfo.objects.get(course_name=course_name)
    # my_obj.delete()

    all_courses = CourseInfo.objects.all()
    return render(request, './starwars/want.html', {'Courses': all_courses})


    

