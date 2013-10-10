# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Equipe'
        db.create_table(u'ligue_equipe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ligue', ['Equipe'])

        # Adding model 'Joueur'
        db.create_table(u'ligue_joueur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'ligue', ['Joueur'])


    def backwards(self, orm):
        # Deleting model 'Equipe'
        db.delete_table(u'ligue_equipe')

        # Deleting model 'Joueur'
        db.delete_table(u'ligue_joueur')


    models = {
        u'ligue.equipe': {
            'Meta': {'object_name': 'Equipe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'ligue.joueur': {
            'Meta': {'object_name': 'Joueur'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ligue']