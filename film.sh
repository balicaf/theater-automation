#!/bin/bash
# at startup, on screen a GUI appears
if zenity --question --text="Are you sure to watch movie?"
then
    continue
else
    exit
fi

python ./begin.py & #power on bulbs
message=$(zenity --file-selection --filename=/media/balicaf/8To/film/) # user select his movie

pkill -USR1 '^redshift$' #redshift is killed in order to have a 6500k screen
python ./end.py & #user has 60 seconds before bulbs are powered off

nvgstplayer -i "$message" -a 30 #movie is hardware decoded and starts at 30seconds
#nvgstplayer -c 2                                   #choose 2nd audio traCk
# mediainfo $message --inform="Audio;%Language%"    #displays available languages
