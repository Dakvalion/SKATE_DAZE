from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


# Register models
admin.site.register(Items, ItemAdmin)
admin.site.register(Reg)
admin.site.register(Mail)
