#!/bin/bash

DIR='/proc/asound/card1/pcm0p/sub0/status'
CMD='python /home/pi/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library/tree.py'

content=''
while true
do
	new_content=`cat $DIR`
	if [[ "$content" != "$new_content" ]]; then
		content=$new_content
		$CMD
	fi
	sleep 0.25
done
