import pycountry
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from .forms import RegisterForm
from .models import Profile, Language, Friend


def index(request):
    if request.user.is_authenticated:
        if not request.user.profile.location or not request.user.profile.primary_language or not request.user.profile.learning_language:
            messages.warning(request, mark_safe("<a href='settings/'>Please complete your profile</a>"))
    profile_list = Profile.objects.all()
    context = {'profile_list': profile_list}
    return render(request, 'mainapp/index.html', context)


@login_required
def profile(request, profile_uuid):
    profile = Profile.objects.get(uuid=profile_uuid)
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


@login_required
def friends(request):
    print(request.POST)
    if request.method == 'POST':
        uuid = request.POST.get('unfriend')
        if request.POST.get('unfriend'):
            friend_obj = Friend.objects.get(
                Q(profile_1=request.user.profile, profile_2=Profile.objects.get(uuid=uuid)) | Q(
                    profile_2=request.user.profile, profile_1=Profile.objects.get(uuid=uuid)))
            friend_obj.delete()

    friend_list = Profile.friend_list(request.user.profile)
    context = {'friend_list': friend_list}
    return render(request, 'mainapp/friends.html', context)


@login_required
def settings(request):
    # debug
    print(request.POST)
    # if form is submitted in setting page we update the profile object
    if request.method == 'POST':
        if request.POST.get('fname'):
            request.user.first_name = request.POST.get('fname')
            request.user.last_name = request.POST.get('lname')
            request.user.email = request.POST.get('email')

            if pycountry.countries.get(name=request.POST.get('location')):  # verify if country name exists
                request.user.profile.location = pycountry.countries.get(
                    name=request.POST.get('location')).alpha_2.lower()  # store 2 letter code in db

        # add a primary language
        if request.POST.get('add_prime_lang'):
            if len(Language.objects.filter(
                    name=request.POST.get('add_prime_lang'))) == 1:  # check if language exist in database
                request.user.profile.primary_language.add(Language.objects.get(name=request.POST.get('add_prime_lang')))
        # removing a primary language
        if request.POST.get('remove_prime_lang'):
            request.user.profile.primary_language.remove(
                Language.objects.get(name=request.POST.get('remove_prime_lang')))
        # add a learning language
        if request.POST.get('add_learn_lang'):
            if len(Language.objects.filter(
                    name=request.POST.get('add_learn_lang'))) == 1:  # check if language exist in database
                request.user.profile.learning_language.add(
                    Language.objects.get(name=request.POST.get('add_learn_lang')))
        # removing a learning language
        if request.POST.get('remove_learn_lang'):
            request.user.profile.learning_language.remove(
                Language.objects.get(name=request.POST.get('remove_learn_lang')))

        request.user.save()  # save user/profile object

    user_prime_lang = request.user.profile.primary_language.all()
    user_learn_lang = request.user.profile.learning_language.all()
    languages = Language.objects.all()
    country_list = pycountry.countries.objects
    context = {'profile': request.user.profile, 'languages': languages, 'user_prime_lang': user_prime_lang,
               'user_learn_lang': user_learn_lang, 'country_list': country_list}
    return render(request, 'mainapp/settings.html', context)
