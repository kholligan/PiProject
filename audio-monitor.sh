#!/bin/bash

DIR='/proc/asound/card0/pcm0p/sub0/status'
CMD='python3 /home/pi/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library/treeClient.py'

content=''
while true
do
	new_content=`cat $DIR`
	if [[ "$content" != "$new_content" ]]; then
		content=$new_content
		$CMD
	fi
	sleep 0.05
done
