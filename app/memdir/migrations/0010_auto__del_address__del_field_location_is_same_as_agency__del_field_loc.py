# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Deleting model 'Address'
        db.delete_table('memdir_address')

        # Deleting field 'Location.is_same_as_agency'
        db.delete_column('memdir_location', 'is_same_as_agency')

        # Deleting field 'Location.name'
        db.delete_column('memdir_location', 'name')

        # Deleting field 'Location.is_default'
        db.delete_column('memdir_location', 'is_default')

        # Deleting field 'Location.place'
        db.delete_column('memdir_location', 'place')

        # Deleting field 'Location.address'
        db.delete_column('memdir_location', 'address')

        # Deleting field 'Location.lat'
        db.delete_column('memdir_location', 'lat')

        # Deleting field 'Location.lng'
        db.delete_column('memdir_location', 'lng')

        # Adding field 'Location.street'
        db.add_column('memdir_location', 'street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.geo_place'
        db.add_column('memdir_location', 'geo_place', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.geo_lat'
        db.add_column('memdir_location', 'geo_lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'Location.geo_lng'
        db.add_column('memdir_location', 'geo_lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'Location.geo_last_updated'
        db.add_column('memdir_location', 'geo_last_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Location.order'
        db.add_column('memdir_location', 'order', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Changing field 'Location.province'
        db.alter_column('memdir_location', 'province', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Location.postal_code'
        db.alter_column('memdir_location', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Deleting field 'Member.site_updated'
        db.delete_column('memdir_member', 'site_updated')

        # Deleting field 'Member.is_subscribed'
        db.delete_column('memdir_member', 'is_subscribed')

        # Deleting field 'Member.is_active'
        db.delete_column('memdir_member', 'is_active')

        # Deleting field 'Member.address'
        db.delete_column('memdir_member', 'address')

        # Deleting field 'Member.next_expiry'
        db.delete_column('memdir_member', 'next_expiry')

        # Deleting field 'Member.rec_upcoming_notice'
        db.delete_column('memdir_member', 'rec_upcoming_notice')

        # Deleting field 'Member.agfax'
        db.delete_column('memdir_member', 'agfax')

        # Deleting field 'Member.name'
        db.delete_column('memdir_member', 'name')

        # Deleting field 'Member.renewal'
        db.delete_column('memdir_member', 'renewal')

        # Deleting field 'Member.successful_location_save'
        db.delete_column('memdir_member', 'successful_location_save')

        # Deleting field 'Member.location'
        db.delete_column('memdir_member', 'location_id')

        # Deleting field 'Member.rec_expiry_notice'
        db.delete_column('memdir_member', 'rec_expiry_notice')

        # Deleting field 'Member.agphone'
        db.delete_column('memdir_member', 'agphone')

        # Adding field 'Member.street'
        db.add_column('memdir_member', 'street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Member.geo_place'
        db.add_column('memdir_member', 'geo_place', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Member.geo_lat'
        db.add_column('memdir_member', 'geo_lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'Member.geo_lng'
        db.add_column('memdir_member', 'geo_lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'Member.geo_last_updated'
        db.add_column('memdir_member', 'geo_last_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Member.phone'
        db.add_column('memdir_member', 'phone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Member.fax'
        db.add_column('memdir_member', 'fax', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Member.renewal_date'
        db.add_column('memdir_member', 'renewal_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Changing field 'Member.postal_code'
        db.alter_column('memdir_member', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Member.province'
        db.alter_column('memdir_member', 'province', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Member.agdirect'
        db.alter_column('memdir_member', 'agdirect', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Member.slug'
        db.alter_column('memdir_member', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

        # Changing field 'Member.join_date'
        db.alter_column('memdir_member', 'join_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2012, 10, 7, 7, 26, 23, 820361), null=True))


    def backwards(self, orm):

        # Adding model 'Address'
        db.create_table('memdir_address', (
            ('province', self.gf('django.db.models.fields.CharField')(default='BC', max_length=2)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('memdir', ['Address'])

        # Adding field 'Location.is_same_as_agency'
        db.add_column('memdir_location', 'is_same_as_agency', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Location.name'
        db.add_column('memdir_location', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.is_default'
        db.add_column('memdir_location', 'is_default', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Location.place'
        db.add_column('memdir_location', 'place', self.gf('django.db.models.fields.CharField')(default='', max_length=200), keep_default=False)

        # Adding field 'Location.address'
        db.add_column('memdir_location', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Location.lat'
        db.add_column('memdir_location', 'lat', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Adding field 'Location.lng'
        db.add_column('memdir_location', 'lng', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True), keep_default=False)

        # Deleting field 'Location.street'
        db.delete_column('memdir_location', 'street')

        # Deleting field 'Location.geo_place'
        db.delete_column('memdir_location', 'geo_place')

        # Deleting field 'Location.geo_lat'
        db.delete_column('memdir_location', 'geo_lat')

        # Deleting field 'Location.geo_lng'
        db.delete_column('memdir_location', 'geo_lng')

        # Deleting field 'Location.geo_last_updated'
        db.delete_column('memdir_location', 'geo_last_updated')

        # Deleting field 'Location.order'
        db.delete_column('memdir_location', 'order')

        # Changing field 'Location.province'
        db.alter_column('memdir_location', 'province', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Location.postal_code'
        db.alter_column('memdir_location', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=7, null=True))

        # Adding field 'Member.site_updated'
        db.add_column('memdir_member', 'site_updated', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 10, 7, 7, 26, 14, 788388), blank=True), keep_default=False)

        # Adding field 'Member.is_subscribed'
        db.add_column('memdir_member', 'is_subscribed', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Member.is_active'
        db.add_column('memdir_member', 'is_active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Member.address'
        db.add_column('memdir_member', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Member.next_expiry'
        db.add_column('memdir_member', 'next_expiry', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Member.rec_upcoming_notice'
        db.add_column('memdir_member', 'rec_upcoming_notice', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.agfax'
        db.add_column('memdir_member', 'agfax', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True), keep_default=False)

        # Adding field 'Member.name'
        db.add_column('memdir_member', 'name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Member.renewal'
        db.add_column('memdir_member', 'renewal', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Member.successful_location_save'
        db.add_column('memdir_member', 'successful_location_save', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.location'
        db.add_column('memdir_member', 'location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='members', null=True, to=orm['memdir.Location'], blank=True), keep_default=False)

        # Adding field 'Member.rec_expiry_notice'
        db.add_column('memdir_member', 'rec_expiry_notice', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Member.agphone'
        db.add_column('memdir_member', 'agphone', self.gf('django.contrib.localflavor.us.models.PhoneNumberField')(max_length=20, null=True, blank=True), keep_default=False)

        # Deleting field 'Member.street'
        db.delete_column('memdir_member', 'street')

        # Deleting field 'Member.geo_place'
        db.delete_column('memdir_member', 'geo_place')

        # Deleting field 'Member.geo_lat'
        db.delete_column('memdir_member', 'geo_lat')

        # Deleting field 'Member.geo_lng'
        db.delete_column('memdir_member', 'geo_lng')

        # Deleting field 'Member.geo_last_updated'
        db.delete_column('memdir_member', 'geo_last_updated')

        # Deleting field 'Member.phone'
        db.delete_column('memdir_member', 'phone')

        # Deleting field 'Member.fax'
        db.delete_column('memdir_member', 'fax')

        # Deleting field 'Member.renewal_date'
        db.delete_column('memdir_member', 'renewal_date')

        # Changing field 'Member.postal_code'
        db.alter_column('memdir_member', 'postal_code', self.gf('django.db.models.fields.CharField')(max_length=7, null=True))

        # Changing field 'Member.province'
        db.alter_column('memdir_member', 'province', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Member.agdirect'
        db.alter_column('memdir_member', 'agdirect', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Member.slug'
        db.alter_column('memdir_member', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=80, unique=True))

        # Changing field 'Member.join_date'
        db.alter_column('memdir_member', 'join_date', self.gf('django.db.models.fields.DateField')(null=True))


    models = {
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'frp_program_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geo_last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geo_lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'geo_lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'geo_place': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mailing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'mailing_province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'}),
            'mailing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'locations'", 'null': 'True', 'to': "orm['memdir.Member']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '10'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
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
            'Meta': {'ordering': "('agency', 'updated')", 'object_name': 'Member'},
            'agdirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agdirect_title': ('django.db.models.fields.CharField', [], {'default': "u'Agency Executive Director / ECD Program Manager'", 'max_length': '255'}),
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'dirphone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fee': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '2', 'blank': 'True'}),
            'geo_last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'geo_lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'geo_lng': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'geo_place': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'join_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'mailing_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mailing_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'mailing_province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '2'}),
            'mailing_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'membership_type': ('django.db.models.fields.CharField', [], {'default': "'joint'", 'max_length': '255'}),
            'memnum': ('django.db.models.fields.IntegerField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paidfrp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'BC'", 'max_length': '10'}),
            'receipt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'renewal_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['memdir']
