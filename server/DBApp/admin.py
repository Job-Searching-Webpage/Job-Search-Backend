from django.contrib import admin
from .models import spotlights, esperienze, teams, backUpPerson, jobs, degrees, dipendenti_user

# Register your models here.

admin.site.register(spotlights)
admin.site.register(esperienze)
admin.site.register(teams)
admin.site.register(backUpPerson)
admin.site.register(jobs)
admin.site.register(degrees)
admin.site.register(dipendenti_user)