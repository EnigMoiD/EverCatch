import re

# Finds #hashtags
tagEx = r"#.+?\b"

def tagNote(note):
	# Removes the hash mark from the hashtag
	# Wraps it in evernote tag tags
	def wrapTag(str):
		return "<tag>"+str[1:]+"</tag>"

	# Only search after the title so that truncated tags aren't found
	# So get the index of the title closing tag
	s = re.search(r"</title>", note).start()

	# Put every #hashtag after the title into a list
	# Convert it to a set and back to make it a unique list
	tags = list(set(re.findall(tagEx, note[s:])))

	# Wrap each tag and join them into one string
	tagString = "".join(map(wrapTag, tags))

	# Substitute that string right before the "<note-attributes/>" tag
	# Add back the note closing tag
	return re.sub("<note-a", tagString+"<note-a", note)+"</note>"

def removeHashes(note):
	def removeHash(matchobj):
		return matchobj.group(0)[1:]

	return re.sub(tagEx, removeHash, note)

def removeHashtags(note):
	return re.sub(tagEx, "", note)