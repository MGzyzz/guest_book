from django.contrib import admin
from .models import Guest_book
# Register your models here.


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email_author', 'time_of_creation', 'edit_time', 'status']
    list_filter = ['name', 'status']
    search_fields = ['name']


admin.site.register(Guest_book, GuestBookAdmin)