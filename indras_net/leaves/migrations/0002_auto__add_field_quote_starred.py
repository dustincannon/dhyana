# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quote.starred'
        db.add_column('leaves_quote', 'starred',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Quote.starred'
        db.delete_column('leaves_quote', 'starred')


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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['leaves.Source']"}),
            'starred': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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