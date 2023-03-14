from django.contrib import admin
from .models import Country, State

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "code", "created_at", "updated_at")
    list_filter = ["name", "code"]
    search_fields = ["name", "code"]
    list_display_links = list_display
    class Meta:
        model = Country

class StateAdmin(admin.ModelAdmin):
    list_display = ("__str__", "name", "code", 'country', "created_at", "updated_at")
    list_filter = ["name", "code", "country"]
    search_fields = ["name", "code", "country"]
    list_display_links = list_display
    class Meta:
        model = State

admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
