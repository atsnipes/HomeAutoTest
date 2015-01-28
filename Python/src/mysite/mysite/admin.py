from django.contrib import admin
from temp.models import TempInput

#mod the admin by adding this
class TempInputAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Current Temperature', {'fields': ['cur_temp']}),
        ('Date Taken', {'fields': ['temp_taken_date'], 'classes': ['collapse']}),
    ]
# Register your models here.
admin.site.register(TempInput,TempInputAdmin)

