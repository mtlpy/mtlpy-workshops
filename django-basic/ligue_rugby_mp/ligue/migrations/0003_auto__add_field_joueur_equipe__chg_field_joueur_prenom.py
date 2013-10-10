# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Joueur.equipe'
        db.add_column(u'ligue_joueur', 'equipe',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ligue.Equipe'], null=True),
                      keep_default=False)


        # Changing field 'Joueur.prenom'
        db.alter_column(u'ligue_joueur', 'prenom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'Joueur.equipe'
        db.delete_column(u'ligue_joueur', 'equipe_id')


        # Changing field 'Joueur.prenom'
        db.alter_column(u'ligue_joueur', 'prenom', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

    models = {
        u'ligue.equipe': {
            'Meta': {'object_name': 'Equipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ligue.joueur': {
            'Meta': {'object_name': 'Joueur'},
            'date_naissance': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'equipe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ligue.Equipe']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prenom': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['ligue']