from django.core import serializers
from memdir.models import Member, Location, HoursOfOperation
from django.http import HttpResponse

def json_page(request, table):
	#Create serializer
	JSONSerializer = serializers.get_serializer('json')
	json_serializer = JSONSerializer()

	#Create response
	response = HttpResponse()

	#Write model data to response
	if table == 'Member':
		response.write(json_serializer.serialize(Member.objects.all()))
	elif table == 'Location':
		response.write(json_serializer.serialize(Location.objects.all()))
	elif table == 'HoursOfOperation':
		response.write(json_serializer.serialize(HoursOfOperation.objects.all()))
	else:
		response.write("Error, table not found.")

	return response
