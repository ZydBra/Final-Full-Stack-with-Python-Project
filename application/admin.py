from django.contrib import admin
from .models import UzrasoKategorija, Uzrasas, User

admin.site.register(User)
admin.site.register(UzrasoKategorija)
admin.site.register(Uzrasas)
