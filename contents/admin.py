from django.contrib import admin
from contents.models import userAdmin,userProfile

# Register your models here.
admin.site.register(userProfile)
admin.site.register(userAdmin)