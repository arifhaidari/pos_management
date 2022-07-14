from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



from .forms import UserAdminCreationForm, UserAdminChangeForm
# from .models import GuestEmail, EmailActivation

User = get_user_model()

# def time_seconds(self, obj):
#          return obj.timefield.strftime("%d %b %Y %H:%M:%S")
# time_seconds.admin_order_field = 'timestamp'
# time_seconds.short_description = 'Precise Time'    

# list_display = ('id', 'time_seconds', )


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('full_name', 'phone', 'business', 'start_contract_at', 'end_contract_at', 'is_active')
    list_filter = ('admin', 'staff', 'is_active')
    fieldsets = [
        (None, {'fields': ('full_name', 'phone', 'plain_password', 'business', 'address', 'access_code', 'password')}),
       # ('Full name', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active',)}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2')}),
    )
    search_fields = ('phone', 'full_name',)
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)



# class EmailActivationAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#
#
#     class Meta:
#         model = EmailActivation
#
#
# admin.site.register(EmailActivation, EmailActivationAdmin)
#
#
# class GuestEmailAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#
#
#     class Meta:
#         model = GuestEmail
#
#
# admin.site.register(GuestEmail, GuestEmailAdmin)
