from django.contrib import admin

# Register your models here.
from .models import Bailarina, Teatro

admin.site.register(Bailarina)
admin.site.register(Teatro)