# part9

* create a script that collect the users logged in and save them in a file Format : timestamp – users
  > #!/bin/bash
  > set +x
  > TIMESTAMP=$(who | awk '{print $3  $4}' | sort | uniq)
  > USERSn=$(who | awk '{print $1}' | sort | uniq)
  > echo " $TIMESTAMP - $USERSn" > /tmp/part9out.txt

* make sure to make the script file execuatble 
  > chmod +x /tmp/part9.sh 

* create a new cronjob using the crontab editor 
  > cronetab -e

* add a job entry that runs every day at 1:30 AM 
  > 30 1 * * * /path to script/part9.sh 
