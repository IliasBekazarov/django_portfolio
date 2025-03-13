from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact  # Туура импорт
from django.shortcuts import render
from .models import AboutMe, Skill, Project, Home, Testimony

def home(request):
    home = Home.objects.first()
    about_me = AboutMe.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    testimonies = Testimony.objects.first()

    context = {
        'home' : home,
        'about_me': about_me,
        'skills': skills,
        'projects': projects,
        'testimonies': testimonies,
    }
    return render(request, 'home.html', context)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        # Валидация
        if len(name) < 2 or len(name) > 30:
            messages.error(request, 'Length of name should be greater than 2 and less than 30 words.')
            return redirect('home')

        if len(email) < 1 or len(email) > 30:
            messages.error(request, 'Invalid email. Please try again.')
            return redirect('home')

        if len(number) < 10 or len(number) > 13:
            messages.error(request, 'Invalid number. Please try again.')
            return redirect('home')

        # Маалыматтарды сактоо
        ins = Contact(name=name, email=email, content=content, number=number)
        ins.save()
        messages.success(request, 'Thank you for contacting me! Your message has been saved.')
        return redirect('home')

    return redirect('home')