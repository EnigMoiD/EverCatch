import simplejson as json
import catchAPI as api
import os, sys, datetime
import re

response = api.get('streams')

streams = response['streams']
		
locations = dict()

for s in streams:
	sNotes = api.get('streams/'+s['id'])['objects']

	name = s['name']

	for n in sNotes:
		note = api.get('streams/'+s['id']+"/"+n['id'])

		if note['type'] == 'note':
			date = note['modified_at']

			latitude = note['annotations'].get('location:latitude', False)
			longitude = note['annotations'].get('location:longitude', False)
			altitude = note['annotations'].get('location:altitude', False)

			if latitude:
				latitude = "<latitude>"+str(latitude)+"</latitude>"
				longitude = "<longitude>"+str(longitude)+"</longitude>"
				altitude = "<altitude>"+str(altitude)+"</altitude>"

				date = re.sub("[-|:|\.]", "", date)

				date = date[:15]+"Z"

				location = latitude+longitude+altitude

				locations[date] = location

path = "~/Desktop/CatchSwitch/" # /locations.json
path = os.path.expanduser(path)
if not os.path.exists(path):
	os.makedirs(path)

f = open(path+"locations.json", "w")
f.write(json.dumps(locations))
print "Done!"