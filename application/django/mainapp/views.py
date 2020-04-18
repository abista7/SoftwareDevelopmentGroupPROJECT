from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Profile, Language


def index(request):
    if request.GET.get('name'):
        profile_list = Profile.objects.filter(name__icontains=request.GET.get('name'))
    elif request.GET.get('gender'):
        profile_list = Profile.objects.filter(gender=request.GET.get('gender'))
    else:
        profile_list = Profile.objects.all()
    context = {'profile_list': profile_list}
    return render(request, 'mainapp/index.html', context)


def profile(request, profile_uuid):
    profile = Profile.objects.get(uuid=profile_uuid)
    user = profile.user
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


def settings(request):
    print(request.POST)
    if request.method == 'POST':
        if request.POST.get('add_prime_lang'):
            request.user.profile.primary_language.add(Language.objects.get(name=request.POST.get('add_prime_lang')))
        if request.POST.get('remove_prime_lang'):
            request.user.profile.primary_language.remove(
                Language.objects.get(name=request.POST.get('remove_prime_lang')))
        if request.POST.get('add_learn_lang'):
            request.user.profile.learning_language.add(Language.objects.get(name=request.POST.get('add_learn_lang')))
        if request.POST.get('remove_learn_lang'):
            request.user.profile.learning_language.remove(
                Language.objects.get(name=request.POST.get('remove_learn_lang')))
    user_prime_lang = request.user.profile.primary_language.all()
    user_learn_lang = request.user.profile.learning_language.all()
    languages = Language.objects.all()
    context = {'profile': request.user.profile, 'languages': languages, 'user_prime_lang': user_prime_lang,
               'user_learn_lang': user_learn_lang}
    return render(request, 'mainapp/settings.html', context)
