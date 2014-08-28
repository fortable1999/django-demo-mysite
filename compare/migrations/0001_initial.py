# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compare'
        db.create_table('compare_compare', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dmm_id1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dmm_id2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dmm_count1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dmm_count2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('compare', ['Compare'])


    def backwards(self, orm):
        # Deleting model 'Compare'
        db.delete_table('compare_compare')


    models = {
        'compare.compare': {
            'Meta': {'ordering': "('created_datetime',)", 'object_name': 'Compare'},
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dmm_count1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dmm_count2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dmm_id1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'dmm_id2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['compare']