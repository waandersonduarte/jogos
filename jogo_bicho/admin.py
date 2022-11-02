from django.contrib import admin
from .models import JogoBicho, Premio
from mega_sena.models import MegaSena

admin.site.register(JogoBicho)
admin.site.register(MegaSena)
admin.site.register(Premio)
