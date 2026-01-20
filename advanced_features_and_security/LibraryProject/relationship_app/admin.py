from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, CustomUser

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Author, AuthorAdmin)

class CustomUserAdmin(UserAdmin):
    # Add custom fields to the user editing page in Admin
    fieldsets = list(UserAdmin.fieldsets) + [
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    ]
    # Add custom fields to the user creation page in Admin
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    ]

admin.site.register(CustomUser, CustomUserAdmin)