from django.contrib import admin

<<<<<<< HEAD

from .models import *

admin.site.register(Profile)
admin.site.register(Post)
=======
from .models import Language, Profile, Friend

import pycountry

>>>>>>> origin/dev-ryan
# Register your models here.
admin.site.register(Language)
admin.site.register(Profile)
admin.site.register(Friend)