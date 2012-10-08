# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Location'
        db.create_table('memdir_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True)),
            ('lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True)),
        ))
        db.send_create_signal('memdir', ['Location'])

        # Adding model 'MemberUser'
        db.create_table('memdir_memberuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='member', unique=True, null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('memdir', ['MemberUser'])

        # Adding model 'Member'
        db.create_table('memdir_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=80, db_index=True)),
            ('memnum', self.gf('django.db.models.fields.IntegerField')()),
            ('renewal', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('agency', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='members', null=True, to=orm['memdir.Location'])),
            ('successful_location_save', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('agphone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('agfax', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('agdirect', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dirphone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('resname', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('frpphone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True)),
            ('coordinator', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('coemail', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('joint', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prior', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('newjoint2009', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('newjoint2010', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('newjoint2011', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('newbc2010', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('frpbcfee', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('jointmemfee', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateField')()),
            ('receipt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('owecanada', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('paidfrpc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('owefrpbc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True)),
            ('paidfrpbc', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('next_expiry', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('site_updated', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('description', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_subscribed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rec_upcoming_notice', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rec_expiry_notice', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('memdir', ['Member'])

        # Adding M2M table for field users on 'Member'
        db.create_table('memdir_member_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm['memdir.member'], null=False)),
            ('memberuser', models.ForeignKey(orm['memdir.memberuser'], null=False))
        ))
        db.create_unique('memdir_member_users', ['member_id', 'memberuser_id'])


    def backwards(self, orm):
        
        # Deleting model 'Location'
        db.delete_table('memdir_location')

        # Deleting model 'MemberUser'
        db.delete_table('memdir_memberuser')

        # Deleting model 'Member'
        db.delete_table('memdir_member')

        # Removing M2M table for field users on 'Member'
        db.delete_table('memdir_member_users')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'memdir.location': {
            'Meta': {'object_name': 'Location'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'memdir.member': {
            'Meta': {'ordering': "('agency', 'site_updated')", 'object_name': 'Member'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'agdirect': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'agfax': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'agphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'coemail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'coordinator': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'dirphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'frpbcfee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'frpphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'joint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jointmemfee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': "orm['memdir.Location']"}),
            'memnum': ('django.db.models.fields.IntegerField', [], {}),
            'newbc2010': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'newjoint2009': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'newjoint2010': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'newjoint2011': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'next_expiry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owecanada': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'owefrpbc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'paidfrpbc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paidfrpc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'prior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'rec_expiry_notice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rec_upcoming_notice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receipt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'renewal': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'resname': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'site_updated': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '80', 'db_index': 'True'}),
            'successful_location_save': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateField', [], {}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'member'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['memdir.MemberUser']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'memdir.memberuser': {
            'Meta': {'object_name': 'MemberUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'member'", 'unique': 'True', 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['memdir']
