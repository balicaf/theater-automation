#!/bin/bash
if zenity --question --text="Are you sure to watch movie?"
then
    continue
else
    exit
fi
python ~/begin.py &
message=$(zenity --file-selection --filename=/media/balicaf/8To/film/)
echo "nvgstplayer -i $message"
pkill -USR1 '^redshift$'
python ~/end.py &
# & not to wait the end of that python
nvgstplayer -i "$message" -a 30
# begin at 30 seconds  -c 2 choose 2nd audio traCk
# mediainfo $message --inform="Audio;%Language%"
