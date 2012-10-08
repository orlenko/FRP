# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Deleting field 'Location.mailing_address'
        db.delete_column('memdir_location', 'mailing_address_id')

        # Adding field 'Location.name'
        db.add_column('memdir_location', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.city'
        db.add_column('memdir_location', 'city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.postal_code'
        db.add_column('memdir_location', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True), keep_default=False)

        # Adding field 'Location.province'
        db.add_column('memdir_location', 'province', self.gf('django.db.models.fields.CharField')(default='BC', max_length=2), keep_default=False)

        # Adding field 'Location.mailing_street'
        db.add_column('memdir_location', 'mailing_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.mailing_city'
        db.add_column('memdir_location', 'mailing_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.mailing_postal_code'
        db.add_column('memdir_location', 'mailing_postal_code', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True), keep_default=False)

        # Adding field 'Location.mailing_province'
        db.add_column('memdir_location', 'mailing_province', self.gf('django.db.models.fields.CharField')(default='BC', max_length=2), keep_default=False)

        # Renaming column for 'Location.address' to match new field type.
        db.rename_column('memdir_location', 'address_id', 'address')
        # Changing field 'Location.address'
        db.alter_column('memdir_location', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Removing index on 'Location', fields ['address']
        db.delete_index('memdir_location', ['address_id'])

        # Deleting field 'Member.mailing_address'
        db.delete_column('memdir_member', 'mailing_address')

        # Deleting field 'Member.mailing_city'
        db.delete_column('memdir_member', 'mailing_city')

        # Deleting field 'Member.mailing_province'
        db.delete_column('memdir_member', 'mailing_province')

        # Deleting field 'Member.mailing_postal_code'
        db.delete_column('memdir_member', 'mailing_postal_code')


    def backwards(self, orm):

        # Adding index on 'Location', fields ['address']
        db.create_index('memdir_location', ['address_id'])

        # Adding field 'Location.mailing_address'
        db.add_column('memdir_location', 'mailing_address', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_mail', null=True, to=orm['memdir.Address']), keep_default=False)

        # Deleting field 'Location.name'
        db.delete_column('memdir_location', 'name')

        # Deleting field 'Location.city'
        db.delete_column('memdir_location', 'city')

        # Deleting field 'Location.postal_code'
        db.delete_column('memdir_location', 'postal_code')

        # Deleting field 'Location.province'
        db.delete_column('memdir_location', 'province')

        # Deleting field 'Location.mailing_street'
        db.delete_column('memdir_location', 'mailing_street')

        # Deleting field 'Location.mailing_city'
        db.delete_column('memdir_location', 'mailing_city')

        # Deleting field 'Location.mailing_postal_code'
        db.delete_column('memdir_location', 'mailing_postal_code')

        # Deleting field 'Location.mailing_province'
        db.delete_column('memdir_location', 'mailing_province')

        # Renaming column for 'Location.address' to match new field type.
        db.rename_column('memdir_location', 'address', 'address_id')
        # Changing field 'Location.address'
        db.alter_column('memdir_location', 'address_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['memdir.Address']))

        # Adding field 'Member.mailing_address'
        db.add_column('memdir_member', 'mailing_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Member.mailing_city'
        db.add_column('memdir_member', 'mailing_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Member.mailing_province'
        db.add_column('memdir_member', 'mailing_province', self.gf('django.db.models.fields.CharField')(default='BC', max_length=2), keep_default=False)

        # Adding field 'Member.mailing_postal_code'
        db.add_column('memdir_member', 'mailing_postal_code', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True), keep_default=False)


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
        'memdir.contactperson': {
            'Meta': {'object_name': 'ContactPerson'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['memdir.Location']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'contact_position': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
        'memdir.member': {
            'Meta': {'ordering': "('agency', 'site_updated')", 'object_name': 'Member'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'agdirect': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'agdirect_title': ('django.db.models.fields.CharField', [], {'default': "u'Agency Executive Director / ECD Program Manager'", 'max_length': '255'}),
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'agfax': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'agphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'coemail': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'coordinator': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'dirphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'frpbcfee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'frpphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_frp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'joint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'jointmemfee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': "orm['memdir.Location']"}),
            'membership_type': ('django.db.models.fields.CharField', [], {'default': "'joint'", 'max_length': '255'}),
            'memnum': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'prior': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'}),
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
