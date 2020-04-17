from django.http import HttpResponse
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
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'mainapp/profile.html', context={'profile': profile})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

