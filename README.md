# theater-automation
The goal of theater-automation is to offer a plug and play experience to watch heavy movie easily on Jetson Nano.
VLC relies on FFMPEG whereas Jetson Nano has only Gstreamer that supports hardware decoding (e.g. to watch 4k h265 movies)

What does this script/code do?
-At startup (When Jetson is booted), a user interface appears that allows the user to select his movie.
-Redshift (equivalent to f.lux) is disabled.
-Lifx lights are powered on for a few minutes to allow user to sit confortably.
-nvgstplayer skips the 30 first seconds of the movie.


prerequisites:
Open your gnome-terminal.
Go to Edit -> Profiles.
Select your Default profile and click on Edit.
Go into "Title and Command" tab.
Select "Run command as login shell" option.
Click on Close button.

https://www.maketecheasier.com/manage-startup-applications-ubuntu/
search "startup application" in ubuntu explorer and add this command at startup
gnome-terminal --command "/path/myscript.sh"

In order to give right access, run this command bellow in the terminal:
chmod 755 "/path/myscript.sh"
