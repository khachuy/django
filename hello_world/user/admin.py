from django.contrib import admin

from .models import Member, Address, Vehicle


class MemberAdmin(admin.ModelAdmin):
    # fields of member
    list_display = ['first_name', 'last_name', 'sex', 'date_of_birth', 'address', 'create_date', 'vehicle']
    # field will use to filter
    list_filter = ['first_name', 'sex', 'address', 'create_date', 'vehicle']
    # field will use to search
    search_fields = ['first_name', 'sex', 'address', 'create_date', 'vehicle']


class AddressAdmin(admin.ModelAdmin):
    # fields of member
    list_display = ['address', 'district']
    # fields will use to filter
    list_filter = ['address', 'district']
    # fields will use to search
    search_fields = ['address', 'district']


class VehicleAdmin(admin.ModelAdmin):
    # fields of member
    list_display = ['vehicle_type', 'vehicle_id']
    # fields will use to filter
    list_filter = ['vehicle_type', 'vehicle_id']
    # fields will use to search
    search_fields = ['vehicle_type', 'vehicle_id']


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Vehicle, VehicleAdmin)

