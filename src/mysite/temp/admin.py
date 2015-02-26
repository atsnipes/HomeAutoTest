from django.contrib import admin
from temp.models import TempInput

#mod the admin by adding this
class TempInputAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Sensor Name', {'fields': ['snsr_name']}),
 ]
# Register your models here.
admin.site.register(TempInput,TempInputAdmin)

