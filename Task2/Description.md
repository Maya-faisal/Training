# Write a script that collects the system performance statistics for cronjob 1
     
   1. CPU Utilization
      
      > cpuUsage=$(top -bn1 | awk '/Cpu/{print $2}')

      **top: shows real-time information about the system's processes** <br/>
      **-b to run in bash mode, meaning it will output the information once and then exit, instead of continuously updating the display** <br/>
      **-n  specifies the number of iterations or updates that top should perform before exiting** <br/>

 2. Memory Usage and Free Memory
     
    > memUsage=$(free -m  | awk '/Mem/{print $3}') <br/>
    > freeMem=$(free -m   | awk '/Mem/{print $4}')

     **free: provides a summary of the system's memory usage** <br/>
     **-m in Megabytes** <br/>
 
  3. Disk  Usage and Free Disk
     A script was written to extract the needed disk and partition data as follows:

     ![image](https://github.com/user-attachments/assets/5ca3adc4-b341-4115-b6aa-8db5f8fe37b2)


  5. Get the TimeStamp
     
     >  TIMESTAMP=$(date '+%Y-%m-%d_%H:%M:%S')   

  6. store each item data in a file named with the item name and the timestamp
     
     > echo "$cpuUsage" >> /Task2/cpu_usage_at_${TIMESTAMP}_.txt  <br/>
     > echo "$freeMem $memUsage" >> /Task2/memory_usage_at_${TIMESTAMP}_.txt

     <br/>
     
# Write a script that calculates the Average of the collected data from cronjob 1, and sends that data to the HTML file, as cronjob 2

 write 3 functions, each iterate through the output files from cronjob1, and calculate the average according to the item format. <br/>
 __Cpu file contains only one value. <br/>__
 __Memory file contains data formatted as following: freeMemory_UsedMemory <br/>__
 __Disk file contains data formatted as follows: disk/partition name_used_avaliable <br/>__

 From each function, there is a data output, that is sent to the HTML elements to be viewed on the web page
 
 ![image](https://github.com/user-attachments/assets/ea5b2d8f-1bc9-4258-afb9-06283e106646)

 
# Install Apache server
  **Install and start the Apache server** <br/>
  > yum install -y httpd <br/>
  > systemctl enable httpd <br/>
  > systemctl start httpd  <br/>  

# Create index.html as the main page for the Web page

  **Create the index.html in var/www/html and add 3 links, each link should direct to a page that displays the average and a list of all the collected item data along with the timestamp** <br/>


# create the cronJobs

**create cronjob1 and cronjob2 and make them run every hour** <br/>
  > crontab -e <br/>
  > 0 * * * * bash Task2/task2.sh && Task2/avg.sh <br/>




      
       
      
