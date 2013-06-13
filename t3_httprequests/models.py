from django.db import models

class HttpRequestLogEntry(models.Model):
    date = models.DateTimeField('Request date/time', db_index=True)
    request_method = models.CharField('Method', max_length=6, db_index=True)
    path = models.CharField(max_length=256)
    query_string = models.CharField(max_length=256)
    priority = models.IntegerField(default=1)

    #http_user_agent = models.CharField(max_length=128)
    #http_referer = models.CharField(max_length=256)
    #remote_addr = models.CharField(max_length=15) #127.000.000.001

    def __unicode__(self):
        return self.path
