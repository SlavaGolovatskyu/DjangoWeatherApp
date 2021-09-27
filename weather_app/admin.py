from django.contrib import admin

from .models import UserIP, City, Support

# Register your models here.
admin.site.register(UserIP)
admin.site.register(City)
admin.site.register(Support)
