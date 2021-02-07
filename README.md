## Spotify-Ad-Mute
This script mutes ads on spotify, runs as python background process. **Windows only**  

### Requirements
Python 3.5+  
pip requires:
 - pip install SwSpotify
 - pip install pycaw
 
### Installation
Download AdMute.pyw and run, really not hard.  
To have it running constantly I suggest adding it to the windows startup folder.

### How it works
Detects the spotify app's name (the title of the application will always change to the song playing) and if the name becomes 'advertisement', mutes the app through windows mixer.
Bare in mind the script checks through every single active application name until it finds 'advertisement' but the names aren't stored.

### Problems
 
Rarely the spotify client thinks its real funny to display the advertisement title name instead of 'advertisement' which the script will not mute. I have an array with names of advertisements that it does it with. It's annoying that i have to manually write it in but there is no other option :/

