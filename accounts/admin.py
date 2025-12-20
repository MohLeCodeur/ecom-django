from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    """Inline pour le profil utilisateur"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profil'


class UserAdmin(BaseUserAdmin):
    """Admin personnalisé pour User avec profil"""
    inlines = (UserProfileInline,)


# Réenregistrer UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'country', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone', 'city']
    list_filter = ['country', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
