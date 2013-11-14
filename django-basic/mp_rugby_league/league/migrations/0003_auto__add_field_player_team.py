# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.team'
        db.add_column(u'league_player', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='teams', null=True, to=orm['league.Team']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.team'
        db.delete_column(u'league_player', 'team_id')


    models = {
        u'league.player': {
            'Meta': {'object_name': 'Player'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams'", 'null': 'True', 'to': u"orm['league.Team']"})
        },
        u'league.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['league']