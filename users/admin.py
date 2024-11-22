from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone', 'role')
    list_filter = ('email', 'first_name', 'last_name', 'phone', 'role')
    search_fields = ('email', 'first_name', 'last_name', 'phone', 'role')
