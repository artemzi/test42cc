from django.contrib import admin

from .models import HttpRequestLog


class HttpRequestLogEntryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'request_method', 'path', 'priority')
    list_display_links = ('__unicode__', 'priority')

    class Meta:
        model = HttpRequestLog

admin.site.register(HttpRequestLog, HttpRequestLogEntryAdmin)