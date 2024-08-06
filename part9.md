# part9

* create a script that collect the users logged in and save them in a file Format : timestamp – users
  > #!/bin/bash <br/>
  > who | while read -r user tty date time _; do <br />
  >  if [ -n "$user" ]; then <br />
  >   LOGIN_TIME="$date $time" <br/>
  >   echo "$LOGIN_TIME – $user" >> user_log_file.txt <br/>
  >  fi <br/>
  > done <br />

* make sure to make the script file execuatble 
  > chmod +x /tmp/part9.sh 

* create a new cronjob using the crontab editor 
  > cronetab -e

* add a job entry that runs every day at 1:30 AM 
  > 30 1 * * * /path to script/part9.sh 
