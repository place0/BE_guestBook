from django.contrib import admin
from .models import GuestBook

#class GuestBookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'author', 'content', 'date')

#admin.site.register(GuestBook, GuestBookAdmin)

admin.site.register(GuestBook)