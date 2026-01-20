from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('title', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

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