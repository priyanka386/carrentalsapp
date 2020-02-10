from django.contrib import admin

# Register your models here.

from .models import Vehicle , Orders , AddCart


admin.site.register(Vehicle)
admin.site.register(Orders)
admin.site.register(AddCart)