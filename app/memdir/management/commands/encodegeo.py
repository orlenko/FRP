from django.core.management.base import BaseCommand, CommandError
from memdir.models import Member, Location
from geopy.geocoders import Google
import time

g = Google()
geocode = g.geocode

class Command(BaseCommand):
    """
    encodes the addresses of the members into a Location()
    """
    args = '<None>'
    help = 'Encodes addresses into lat & lng for all Members()'
    def handle(self, *args, **options):
        members = Member.objects.all()
        for mem in members:
            for location in mem.locations:
                try:
                    try:
                        place, (lat, lng) = geocode(location.geo_address)
                    except:
                        print "there was a geocode error"
                    time.sleep(0.25)
                    l = Location(
                            place=place,
                            lat = "%s" % lat,
                            lng = "%s" % lng,
                        )
                    try:
                        l.save()
                    except:
                        print "There was an issue saving the location"
                    location.location = l
                    try:
                        mem.successful_location_save = True
                        mem.save()
                    except:
                        print "There was an issue saving the member"
                    print "Agency %(agency)s address was saved successfully.\
                            Saved geoaddress %(geoaddress)s to lat: %(lat)s, lng: %(lng)s" % {
                                    'agency': mem.agency,
                                    'geoaddress': mem.geo_address,
                                    'lat': mem.location.lat,
                                    'lng': mem.location.lng,
                                }
    
                except:
                    mem.successful_location_save = False
                    mem.save()
                    print "Agency %(agency)s address raised an error. Tried to\
                        save geoaddress %(geoaddress)s" % {
                                    'agency': mem.agency,
                                    'geoaddress': mem.geo_address,
                                }


