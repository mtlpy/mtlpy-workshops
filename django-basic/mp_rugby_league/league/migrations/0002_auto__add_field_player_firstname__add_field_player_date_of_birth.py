# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.firstname'
        db.add_column(u'league_player', 'firstname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Player.date_of_birth'
        db.add_column(u'league_player', 'date_of_birth',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.firstname'
        db.delete_column(u'league_player', 'firstname')

        # Deleting field 'Player.date_of_birth'
        db.delete_column(u'league_player', 'date_of_birth')


    models = {
        u'league.player': {
            'Meta': {'object_name': 'Player'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'league.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['league']