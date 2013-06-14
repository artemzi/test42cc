# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestLogEntry'
        db.create_table(u't3_httprequests_httprequestlogentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(db_index=True)),
            ('request_method', self.gf('django.db.models.fields.CharField')(max_length=6, db_index=True)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('query_string', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u't3_httprequests', ['HttpRequestLogEntry'])


    def backwards(self, orm):
        # Deleting model 'HttpRequestLogEntry'
        db.delete_table(u't3_httprequests_httprequestlogentry')


    models = {
        u't3_httprequests.httprequestlogentry': {
            'Meta': {'object_name': 'HttpRequestLogEntry'},
            'date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'query_string': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'request_method': ('django.db.models.fields.CharField', [], {'max_length': '6', 'db_index': 'True'})
        }
    }

    complete_apps = ['t3_httprequests']