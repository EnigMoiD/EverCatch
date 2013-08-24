import sys, os
import re
import TagNote, LocateNote

# overwrites a file with its tagged version
def processFile(path, arg="hash"):
	f = open(path, "r")
	notesText = f.read()

	# Splits an enex containing multiple notes into a list of those notes
	noteTexts = re.split("</note>", notesText)

	# Pops off the </en-export> and saves it for later
	end = noteTexts.pop()

	# Call tagNote() on each note in the list
	# Join the results into one string
	# And add the end-of-file tag back on to the string
	newNote = "".join(map(TagNote.tagNote, noteTexts))+end

	# Splits an enex containing multiple notes into a list of those notes
	noteTexts = re.split("</note>", newNote)

	# Pops off the </en-export> and saves it for later
	end = noteTexts.pop()

	# Call locateNote() on each note in the list
	# Join the results into one string
	# And add the end-of-file tag back on to the string
	newNote = "".join(map(LocateNote.locateNote, noteTexts))+end

	# Handle arguments
	if arg == "dehash":
		newNote = TagNote.removeHashes(newNote)
	elif arg == "dehashtag":
		newNote = TagNote.removeHashtags(newNote)

	f = open(path, "w")
	# Overwrite the old file (advise to make a copy first!)
	f.write(newNote)

# Recursively walks the Catch Notes directory, tagging every enex file
for dirname, dirnames, filenames in os.walk(sys.argv[1]):
	for filename in filenames:
		if re.search(r"enex$", filename):
			path = os.path.join(dirname, filename)

			# Only pass an argument if one exists
			if len(sys.argv) > 2:
				processFile(path, sys.argv[2])
			else: processFile(path)