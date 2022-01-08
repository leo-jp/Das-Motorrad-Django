from django.contrib import admin

from . import models

class MotorräderAdmin(admin.ModelAdmin):
    list_display = ('brand',)

admin.site.register(models.Motorräder, MotorräderAdmin)