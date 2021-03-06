from django.contrib import admin

from core.models import Dog, AdoptionApplication, Event


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass


@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'dog',
        'applicant_name',
        'applied_at',
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    exclude = ('slug',)
