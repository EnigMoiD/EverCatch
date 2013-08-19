import simplejson as json
import catchAPI as api
import os, sys, datetime
import re

def locateNote(note):
	f = open("/Users/Enigmoid/Desktop/tmp/locations.json", "r")
	locations = json.loads(f.read())

	date = re.search(r"<updated>.*?</updated>", note).group(0)
	date = re.search(r">.*?<", date).group(0)
	date = date[1:]

	date = date[:-1]

	location = locations.get(str(date), False)

	print location

	newNote = note
	if location:
		newNote = re.sub("</note-a", location.encode('utf-8')+"</note-a", note)+"</note>"
	else: newNote = newNote+"</note>"

	return newNote