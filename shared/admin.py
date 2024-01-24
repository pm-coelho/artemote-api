from django.contrib import admin

from shared.models import Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
