# part6

* write a script that runs for 10mins without doing anything located in /tmp files


  #!/bin/bash  <br /> end=$((SECONDS+600)) <br /> while [ $SECONDS -lt $end ];  <br /> do <br />    sleep 1  <br /> done

* change the permissions for the script file to make it executable 
  > chmod +x /tmp/part6.sh

* run the script in the background
  > ./part6.sh &

  ![Capture0](https://github.com/user-attachments/assets/8904dcdf-d1be-4d8f-883e-80ef722fb2e7)


* search using the PID for the process to track it 
  > ps aux | grep  24301
  
  ![Capture1](https://github.com/user-attachments/assets/fdb73da4-106a-48c0-8c26-b13cf98a40d1)


* kill the process by sending a kill signal to the PID
  > kill -9  24301
  
  ![Capture](https://github.com/user-attachments/assets/7dd9787c-8a13-43cc-8b20-62627c4d3096)

