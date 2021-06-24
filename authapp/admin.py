from django.contrib import admin
from authapp.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    fields = (('first_name', 'last_name'), 'email', 'image')
    ordering = ('last_name', 'first_name')
    search_fields = ('email',)
