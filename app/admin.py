from django.contrib import admin
from .models import Meeting

class MeetingAdmin(admin.ModelAdmin):
    list_display=('id','title','description','start_time', 'end_time' )
admin.site.register(Meeting, MeetingAdmin)