from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = (
        "username",
        "email",
        "role",
        "is_active",
        "is_staff",
    )
    list_filter = (
        "role",
        "is_active",
        "is_superuser",
        "date_joined",
    )
    search_fields = (
        "email",
        "username",
        "first_name",
        "last_name",
        "role",
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": (
            "avatar",
            "bio",
            "role",
        ), }), 
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": (
            "avatar",
            "email",
            "first_name",
            "last_name",
            "bio",
        ), }), 
    )
