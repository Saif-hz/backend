from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Artist, Producer

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_active', 'is_staff')  # Supprimé nom, prenom, role
    list_filter = ('is_active', 'is_staff')  # Supprimé role

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'prenom', 'talents', 'genres')  # Supprimé role
    fields = ('email', 'nom', 'prenom', 'profile_picture', 'bio', 'talents', 'genres')

admin.site.register(Artist, ArtistAdmin)

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('email', 'nom', 'prenom', 'studio_name', 'website', 'genres')  # Supprimé role
    fields = ('email', 'nom', 'prenom', 'profile_picture', 'bio', 'studio_name', 'website', 'genres')

admin.site.register(Producer, ProducerAdmin)
