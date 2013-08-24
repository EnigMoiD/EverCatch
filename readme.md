EverCatch
===
Improve Catch Notes Evernote export by adding tags and locations.

---

EverCatch uses the Catch API v3 to add location metadata back to your notes, and uses regular expressions to turn your Catch #tags into native Evernote tags.

###Explanation

EverCatch consists of a few Python scripts that work together to

1. Pull location metadata from your notes via the Catch API
2. Process your exported Catch Notes to add location and tag metadata.

###Configuration

######Account Requirements

Unfortunately, since I didn't want to build my own API and host a website just to populate my notes with metadata, you must have a "native" Catch account that doesn't use Google, Facebook, or any other signin. But if you do (as I did), not all is lost!

Create a new account with just a username and password, and you can share all your spaces to that account. Unfortunately, this is a manual process, and may vary in time depending on how many spaces you have.

More unfortunately, as your default "Ideas" space cannot be shared, any notes whose metadata you would like to preserve must be (again, manually) moved to another space, and then that space shared.

######Catch Export

Export all your Catch notes via zip file via Catch's [website](http://support.catch.com/customer/portal/articles/988949-how-can-i-export-notes-on-the-web-interface).

######Script Configuation

Once you have a straight "Catch" account, have exported your Catch notes, and have downloaded/cloned this repository, fill in your username and password in `catchAPI.py` where indicated:

```
username = "#Enter your username"
password = "#Enter your password"
```

These will be used to access your account information with basic HTTP authentication. It's not as secure as OAuth, but we're only making one request.

###Usage

Before anything else, make a local copy of your exported Catch notes! This script is not known to do anything bad or wrong, but it does edit the files in place, so be warned.

First, from your command line, in your local repository root, run

`$ python getLocations.py`

This may take a while, depending on how many notes you have.

When the script finishes executing you will now have `~/Desktop/EverCatch/locations.json`. The next script uses this file.

Run that script with

`$ python everCatch.py Path/to/Catch\ Notes <hash-option>`

Where

- `Path/to/Catch\ Notes` is the path to the folder containing your exported Catch notes
- `<hash-option>` is either
	- `dehash`, to remove # from tags as they appear in the note text,
	- `dehashtag`, to remove the entire tag as it would have appeared in the note text,
	- Or blank. `<hash-option>` is optional; leave blank to keep the note text untouched.
	
######Success!

Once `everCatch.py` has finished running, every single `.enex` file in every subdirectory of your Catch Notes directory has all its associated location metadata and tags, ready for Evernote import! You are free to import all your notes at once, or to import in multiple steps, and your metadata will still be preserved.

###Motivation

Like many Catch Notes users, I was disappointed when Catch announced the closing of their service. I was also disappointed with Catch's export tool, which preserved no metadata.

So I decided to use the Catch Notes API to pull that metadata into Catch's `.enex` files for import into Evernote.

###Help!

Unfortunately, there's not much time before Catch Notes shuts down, assumedly along with its API. But if anyone is much better acquainted than me with the Catch API v3 (much more poorly-documented than v2), and you perhaps have an idea on how to pull media into notes in a similar way that I pulled in location metadata, let me know! Fork, pull request, whatever. Before it's too late!

And of course, please contact me with any questions, concerns, suggestions, feedback, gratitude, ingratitude, etc. And spread the word! I wrote this tool to help myself, but I'm releasing it to help others. Help me help everyone!