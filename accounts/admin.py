from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.http.request import HttpRequest
from django.utils.translation import gettext_lazy as _
from profiles.models import Profile

from accounts.models import CustomUser
from accounts.services import UserService

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 5


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    list_display = [
        "id",
        "email",
        "is_admin",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
    ]
    ordering = ["email", "created_at", "is_admin"]

    list_display_links = ("id", "email")

    search_fields = ["email"]
    list_filter = ["is_active", "is_admin", "is_superuser"]
    filter_horizontal = ("groups", "user_permissions")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Booleans"), {"fields": ("is_active", "is_admin", "is_superuser")}),
        (_("Permissions"), {"fields": ("groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {"fields": ("email", "password1", "password2")}),
        (_("Booleans"), {"fields": ("is_admin", "is_superuser", "is_active")}),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    def save_model(
        self,
        request: HttpRequest,
        obj: CustomUser,
        form: ModelForm,
        change: bool,
    ) -> None:
        if change:
            return super().save_model(request, obj, form, change)
        try:

            data: dict = form.cleaned_data
            password = data.pop("password1")
            data.pop("password2")
            data["password"] = password

            UserService.create(**data)
        except ValidationError as exc:
            self.message_user(
                request=request,
                message=str(exc),
                level=messages.ERROR,
            )
