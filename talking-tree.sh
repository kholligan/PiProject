#!/bin/bash
source env/bin/activate
killall audio-monitor.sh
killall python3
assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library/audio-monitor.sh &
python3 assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library/treeServer.py &
python3 assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library/hotword.py --device_model_id talkingtree-pi1
