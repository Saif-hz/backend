from django.contrib import admin
from .models import User, Artist, Producer, Talent, Genre

# Enregistrement simple des modèles dans Django Admin
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Producer)
admin.site.register(Talent)
admin.site.register(Genre)
