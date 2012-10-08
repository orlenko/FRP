# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Member.jointmemfee'
        db.delete_column('memdir_member', 'jointmemfee')

        # Deleting field 'Member.newbc2010'
        db.delete_column('memdir_member', 'newbc2010')

        # Deleting field 'Member.newjoint2009'
        db.delete_column('memdir_member', 'newjoint2009')

        # Deleting field 'Member.paidfrpc'
        db.delete_column('memdir_member', 'paidfrpc')

        # Deleting field 'Member.paidfrpbc'
        db.delete_column('memdir_member', 'paidfrpbc')

        # Deleting field 'Member.joint'
        db.delete_column('memdir_member', 'joint')

        # Deleting field 'Member.coemail'
        db.delete_column('memdir_member', 'coemail')

        # Deleting field 'Member.owecanada'
        db.delete_column('memdir_member', 'owecanada')

        # Deleting field 'Member.is_frp'
        db.delete_column('memdir_member', 'is_frp')

        # Deleting field 'Member.frpphone'
        db.delete_column('memdir_member', 'frpphone')

        # Deleting field 'Member.coordinator'
        db.delete_column('memdir_member', 'coordinator')

        # Deleting field 'Member.frpbcfee'
        db.delete_column('memdir_member', 'frpbcfee')

        # Deleting field 'Member.newjoint2011'
        db.delete_column('memdir_member', 'newjoint2011')

        # Deleting field 'Member.newjoint2010'
        db.delete_column('memdir_member', 'newjoint2010')

        # Deleting field 'Member.owefrpbc'
        db.delete_column('memdir_member', 'owefrpbc')

        # Deleting field 'Member.prior'
        db.delete_column('memdir_member', 'prior')

        # Deleting field 'Member.resname'
        db.delete_column('memdir_member', 'resname')

        # Adding field 'Member.fee'
        db.add_column('memdir_member', 'fee', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True), keep_default=False)

        # Adding field 'Member.paidfrp'
        db.add_column('memdir_member', 'paidfrp', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.join_date'
        db.add_column('memdir_member', 'join_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Changing field 'Member.updated'
        db.alter_column('memdir_member', 'updated', self.gf('django.db.models.fields.DateField')(auto_now=True))


    def backwards(self, orm):
        
        # Adding field 'Member.jointmemfee'
        db.add_column('memdir_member', 'jointmemfee', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True), keep_default=False)

        # Adding field 'Member.newbc2010'
        db.add_column('memdir_member', 'newbc2010', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.newjoint2009'
        db.add_column('memdir_member', 'newjoint2009', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.paidfrpc'
        db.add_column('memdir_member', 'paidfrpc', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.paidfrpbc'
        db.add_column('memdir_member', 'paidfrpbc', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.joint'
        db.add_column('memdir_member', 'joint', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.coemail'
        db.add_column('memdir_member', 'coemail', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True), keep_default=False)

        # Adding field 'Member.owecanada'
        db.add_column('memdir_member', 'owecanada', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True), keep_default=False)

        # Adding field 'Member.is_frp'
        db.add_column('memdir_member', 'is_frp', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Member.frpphone'
        db.add_column('memdir_member', 'frpphone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Member.coordinator'
        db.add_column('memdir_member', 'coordinator', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True), keep_default=False)

        # Adding field 'Member.frpbcfee'
        db.add_column('memdir_member', 'frpbcfee', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True), keep_default=False)

        # Adding field 'Member.newjoint2011'
        db.add_column('memdir_member', 'newjoint2011', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.newjoint2010'
        db.add_column('memdir_member', 'newjoint2010', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.owefrpbc'
        db.add_column('memdir_member', 'owefrpbc', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=2, blank=True), keep_default=False)

        # Adding field 'Member.prior'
        db.add_column('memdir_member', 'prior', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.resname'
        db.add_column('memdir_member', 'resname', self.gf('django.db.models.fields.CharField')(default='', max_length=180), keep_default=False)

        # Deleting field 'Member.fee'
        db.delete_column('memdir_member', 'fee')

        # Deleting field 'Member.paidfrp'
        db.delete_column('memdir_member', 'paidfrp')

        # Deleting field 'Member.join_date'
        db.delete_column('memdir_member', 'join_date')

        # Changing field 'Member.updated'
        db.alter_column('memdir_member', 'updated', self.gf('django.db.models.fields.DateField')())


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
        'memdir.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'})
        },
        'memdir.hoursofoperation': {
            'Meta': {'object_name': 'HoursOfOperation'},
            'close_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime.now'}),
            'day': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hours_of_operation'", 'to': "orm['memdir.Location']"}),
            'open_time': ('django.db.models.fields.TimeField', [], {'default': 'datetime.datetime.now'})
        },
        'memdir.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'frp_program_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_same_as_agency': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mailing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'mailing_province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'}),
            'mailing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'locations'", 'null': 'True', 'to': "orm['memdir.Member']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'})
        },
        'memdir.locationcontact': {
            'Meta': {'object_name': 'LocationContact'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['memdir.Location']"})
        },
        'memdir.member': {
            'Meta': {'ordering': "('agency', 'site_updated')", 'object_name': 'Member'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'agdirect': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'agdirect_title': ('django.db.models.fields.CharField', [], {'default': "u'Agency Executive Director / ECD Program Manager'", 'max_length': '255'}),
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'agfax': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'agphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'dirphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': "orm['memdir.Location']"}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mailing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'mailing_province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'}),
            'mailing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'membership_type': ('django.db.models.fields.CharField', [], {'default': "'joint'", 'max_length': '255'}),
            'memnum': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'next_expiry': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paidfrp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'}),
            'rec_expiry_notice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rec_upcoming_notice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'receipt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'renewal': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'site_updated': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '80', 'db_index': 'True'}),
            'successful_location_save': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
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
