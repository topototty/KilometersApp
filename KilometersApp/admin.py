from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', )
    list_filter = ('user__is_staff',)

    def get_encrypted_phone(self, obj):
        return obj.encrypted_phone
    get_encrypted_phone.short_description = 'Зашифрованный номер телефона'

admin.site.register(Profile, ProfileAdmin)
