# part6

* script that runs for 10mins without doing anything located in /tmp files


#!/bin/bash

# Run the script for 10 minutes 
end=$((SECONDS+600))

while [ $SECONDS -lt $end ]; do
    sleep 1
done

* run the script in the background
  > ./part6.sh &


* change the permissions for the script file to make t executable 
  > chmod +x /tmp/part6.sh

* search using the PID for the process to track it 
  > ps aux | grep  24301

* kill the process by sending a kill signal to the PID
  > kill -9  24301
