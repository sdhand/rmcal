# rmcal

This is a (very) hacky solution to get a calendar with events from an ical source (google calendar, outlook, etc.) onto the remarkable, with pages for diary entries/weekly todos etc.

The code was written without much (any) prethought or planning, and I basically just took the easiest fix for each problem as it cropped up, so there are countless ways in which it could be improved. The dependencies are a texlive installation, and the icalevents python package.

For setup, place the files in this repo on some (non remarkable) machine, and edit `generate.sh` to add an ical link that the calendar will be populated from. (To get this link for google calendar see the "view only" section [here](https://support.google.com/calendar/answer/37648).)

Then setup a cronjob/systemd timer to run generate.sh every few hours or so, this will generate a Calendar.pdf in the directory in which the script is placed.

Finally, to get the pdf onto the remarkable you could either try using https://github.com/juruen/rmapi, although I had limited success with this. 
Or, just copy it to the device once manually, and determine what its resulting filename is in .local/share/remarkable/xochitl. Then setup a systemd timer on the remarkable to copy the generated file from the machine on which this repo is hosted and replace the pdf in the remarkable's file tree.

## Calendar format
The current generation of the calendar is very much based around my own personal organisation preferences, but it shouldn't be too hard to modify (just don't look too closely at my LaTeX).

Pressing the day number in any calendar cell will take you to a page where you can create notes/diary entries for that particular day. There is an exit button at the top of these notes pages to return to the main calendar.

Pressing the tick in the monday calendar cells will take you to a page where you can create a todo list for that week.

Finally, some photos:

![Main calendar](https://i.imgur.com/mB22hSA.jpg)
![Day notes](https://i.imgur.com/slH0CTL.jpg)
![Weekly todo](https://i.imgur.com/H11gzI7.jpg)
