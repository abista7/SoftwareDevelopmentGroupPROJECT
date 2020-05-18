from django.contrib import admin

from .models import *
import pycountry


# Register your models here.
admin.site.register(Language)
admin.site.register(Profile)
admin.site.register(Friend)
admin.site.register(Post)