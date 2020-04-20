import pycountry
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from .forms import RegisterForm
from .models import Profile, Language, Friend, get_profile_model, friend_relation, Post
from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        # display message if user has incomplete section in settings
        if not request.user.profile.location or not request.user.profile.primary_language or not request.user.profile.learning_language:
            messages.warning(request, mark_safe("<a href='settings/'>Please complete your profile</a>"))

        if request.method == 'POST':
            print(request.POST)
            if request.POST.get('add_friend'):
                request.user.profile.add_friend(request.POST.get('add_friend'))
            if request.POST.get('accept_friend_request'):
                request.user.profile.accept_friend_request(request.POST.get('accept_friend_request'))
            if request.POST.get('cancel_friend_request'):
                request.user.profile.cancel_friend_request(request.POST.get('cancel_friend_request'))
            if request.POST.get('decline_friend_request'):
                request.user.profile.decline_friend_request(request.POST.get('decline_friend_request'))

        # matching:
        profile = request.user.profile
        query_set = set([])
        for prime_lang in profile.primary_language.all():
            query = get_profile_model().filter(learning_language__name=prime_lang.name)
            for item in query:
                if not friend_relation(profile, item):
                    query_set.add(item)
        for learn_lang in profile.learning_language.all():
            query = get_profile_model().filter(primary_language__name=learn_lang.name)
            for item in query:
                if not friend_relation(profile, item):
                    query_set.add(item)

        context = {'profile_list': query_set}
        return render(request, 'mainapp/index.html', context)
    else:
        return render(request, 'mainapp/home.html')


# def profile(request, profile_id):
#     profile = get_object_or_404(Profile, pk=profile_id)
#     post_list = Post.objects.filter(profile=profile)
#     return render(request, 'mainapp/profile.html', context={'profile': profile, 'post_list': post_list})

@login_required
def profile(request, profile_uuid):
    profile = get_profile_model().get(uuid=profile_uuid)
    post_list = Post.objects.filter(profile=profile)
    context = {'profile': profile, 'post_list': post_list}
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



def homepage(request):
    username = request.user.get_username()
    userProfile = Profile.objects.get(user=request.user)
    return render(request, 'mainapp/homepage.html', context={'username': username, 'profile': userProfile})


@login_required
def friends(request):
    print(request.POST)
    if request.method == 'POST':
        uuid = request.POST.get('unfriend')
        if request.POST.get('unfriend'):
            friend_obj = Friend.objects.get(
                Q(profile_1=request.user.profile, profile_2=get_profile_model().get(uuid=uuid)) | Q(
                    profile_2=request.user.profile, profile_1=get_profile_model().get(uuid=uuid)))
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

        # about me
        if request.POST.get('about_me'):
            request.user.profile.about_me = request.POST.get('about_me')

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


def setup(request):
    lang_list_alpha_3 = ['spa', 'fra', 'deu', 'eng', 'jpn', 'ita', 'zho', 'ara', 'rus', 'kor', 'por', 'heb', 'hin',
                         'nep', 'fas', 'tgl', 'hin', 'afr', 'nld', 'ben', 'tur', 'swa', 'urd']

    lang_list_alpha_3.sort()
    lang_names = []
    for lang in lang_list_alpha_3:
        lang_names.append(pycountry.languages.get(alpha_3=lang).name)
        obj, created = Language.objects.get_or_create(alpha_3=lang, name=pycountry.languages.get(alpha_3=lang).name)
        if created:
            str(obj) + ' was added to database'

    print('language database addition script finished successfully')

    return HttpResponse('Script Ran')

