from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from profiles.models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "account",
        "maturity_rating",
        "kid_profile",
    )

    list_filter = ("kid_profile", "is_active", "maturity_rating")
    list_select_related = ("account",)
    search_fields = ["name", "account__email"]
    ordering = ("account",)

    fieldsets = (
        (None, {"fields": ("name",)}),
        (_("Account"), {"fields": ("account",)}),
        (_("Parental Rating"), {"fields": ("maturity_rating", "kid_profile")}),
        (_("Booleans"), {"classes": ("collapse",), "fields": ("is_active",)}),
        (_("Important dates"), {"fields": ("created_at", "updated_at")}),
    )
    # add_fieldsets

    readonly_fields = ("created_at", "updated_at")
