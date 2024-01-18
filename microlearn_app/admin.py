from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']
    

# #if we need to add additional field, this is how to do it
# #Assume 'phone_number' is a custom field you added:
    
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number',)}),
#     )

admin.site.register(CustomUser, CustomUserAdmin)
