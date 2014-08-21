# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CourseMode'
        db.create_table('auth_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school_name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('school', ['School'])


    def backwards(self, orm):
        # Deleting model 'CourseMode'
        db.delete_table('auth_school')


    models = {
        'auth_school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
        }
    }

    complete_apps = ['school']