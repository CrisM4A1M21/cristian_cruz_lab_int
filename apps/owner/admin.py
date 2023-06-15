from django.contrib import admin
from apps.owner.models import Owner


#admin.site.register(Owner)
@admin.register(Owner)
class OwnerAmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "vigente")
    list_filter = ("pais",)
    search_fields = ("nombre", "pais")
    fields = ("nombre", "pais")
