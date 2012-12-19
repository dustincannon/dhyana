# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table('leaves_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=400)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('leaves', ['Author'])

        # Adding model 'Source'
        db.create_table('leaves_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=400)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(default='Website', max_length=400)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=2048, null=True, blank=True)),
        ))
        db.send_create_signal('leaves', ['Source'])

        # Adding model 'Quote'
        db.create_table('leaves_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')(unique=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['leaves.Author'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['leaves.Source'])),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('leaves', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table('leaves_author')

        # Deleting model 'Source'
        db.delete_table('leaves_source')

        # Deleting model 'Quote'
        db.delete_table('leaves_quote')


    models = {
        'leaves.author': {
            'Meta': {'object_name': 'Author'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '400'})
        },
        'leaves.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaves.Author']"}),
            'body': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaves.Source']"})
        },
        'leaves.source': {
            'Meta': {'object_name': 'Source'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'Website'", 'max_length': '400'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '400'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['leaves']