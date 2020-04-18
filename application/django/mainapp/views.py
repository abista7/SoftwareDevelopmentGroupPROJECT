from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegisterForm
from .models import Profile


def index(request):
    if request.GET.get('name'):
        profile_list = Profile.objects.filter(name__icontains=request.GET.get('name'))
    elif request.GET.get('gender'):
        profile_list = Profile.objects.filter(gender=request.GET.get('gender'))
    else:
        profile_list = Profile.objects.all()
    context = {'profile_list': profile_list}
    return render(request, 'mainapp/index.html', context)


def profile(request, profile_id):
    if profile_id:
        user = get_object_or_404(get_user_model(), pk=profile_id)
    else:
        user = get_object_or_404(get_user_model(), pk=request.user.pk)
    profile = user.profile
    primary_lang = ''
    for lang in profile.primary_language.all():
        primary_lang += lang.name + ' '
    learning_lang = ''
    for lang in profile.learning_language.all():
        learning_lang += lang.name + ' '

    context = {'profile': profile, 'learning_lang': learning_lang, 'primary_lang': primary_lang}
    return render(request, 'mainapp/profile.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
