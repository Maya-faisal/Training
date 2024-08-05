# part9

* create a script that collect the users logged in and save them in a file Format : timestamp – users
  
  ![Capture4](https://github.com/user-attachments/assets/91c4235a-55c4-4b96-9067-74dcc804833e)


* make sure to make the script file execuatble 
  > chmod +x /tmp/part9.sh 

* create a new cronjob using the crontab editor 
  > cronetab -e

* add a job entry that runs every day at 1:30 AM 
  > 30 1 * * * /path to script/part9.sh 
