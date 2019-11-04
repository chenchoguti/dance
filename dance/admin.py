from django.contrib import admin

# Register your models here.
from .models import Bailarina, BailarinaAdmin, Teatro, TeatroAdmin, Nacionalidad

admin.site.register(Bailarina, BailarinaAdmin)
admin.site.register(Teatro, TeatroAdmin)
admin.site.register(Nacionalidad)