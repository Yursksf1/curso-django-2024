from django.contrib import admin
from myapp.models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]
    search_fields = ["first_name", "last_name"]


admin.site.register(Person, PersonAdmin)