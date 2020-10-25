from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'vector',
    )


admin.site.register(Person, PersonAdmin)