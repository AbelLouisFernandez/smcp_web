from django.contrib import admin

from .models import person, family, bcc_unit, parishpreist

admin.site.register(person)
admin.site.register(family)
admin.site.register(bcc_unit)
admin.site.register(parishpreist)