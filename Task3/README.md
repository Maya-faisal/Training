# GET APIs <br/>
**6 APIs required, <br/>
 3 for the statistics for each hour in the last 24 hours, and was done using cronjobs to collect the data <br/>
 3 for current Memory/CPU/Disk usage, and was collected using Python modules**

  ![image](https://github.com/user-attachments/assets/86c6f307-f3ef-4769-b545-53d899fa7b3d)

# Logging
**Logging is configured to write INFO level messages and above to a file named log.log. <br/>**

**A logger object is created using logging.getLogger(__name__). Additionally, a decorator is applied to functions to automatically log their calls and results.<br/>**

**The @wraps(fn) decorator ensures the wrapper retains the original function’s metadata.**

![image](https://github.com/user-attachments/assets/b9ce2a41-b1bc-4732-8963-7fcbf4eeda0d)

# Unit-Testing
**Three test were implemented<br/>**
**1. Test the Humanize value function, that converts the collected data to Human readable values<br/>**
**2. Test Database connection and Data Insertion<br/>**
**3. Test the Flask App routes<br/>**

![image](https://github.com/user-attachments/assets/a4c7df81-4cd3-4f8f-be27-72c5cc3d2576)
<br/>

> python3 -m unit_tets.py -v <br/>

![image](https://github.com/user-attachments/assets/a7bef8ae-68dc-45c1-bba9-1a03bb1af408)


# DataBase
**Maria DataBase was used to store the data**

 ![image](https://github.com/user-attachments/assets/4571bef5-6a14-47f9-a707-ddb59a3dbd33)

 <br/>
 
 >mariadb -u root -p <br/>
 
 ![image](https://github.com/user-attachments/assets/657ec732-0e41-4dc2-9f4c-b2d66c8a4350)


# Docker and Containerization
**1. First, create the Dockerfile for the Flask App** <br/>

  __install python base image__ <br/>
  __install all required modules__ <br/>
  __copy needed files and directories__ <br/> 
  __pass the environment variables for the Flask App__ <br/>
  __pass the CMD to run the flask app, bash and python scripts responsible for collecting data__ <br/>

**The start.sh script file starts the cronjobs and the flask App**<br/>

>#!/bin/sh<br/>
>#Start the Flask app<br/>
>flask run --host=0.0.0.0 &<br/>
>#Start cron in the foreground<br/>
>cron -f<br/>

**2. Create the docker-compose file**<br/>

**Create the compose file that links the app with the database, and pass the database credentials.<br>
It builds the flask app image with tag v1 and host it on port 5000, mariadb image on port 3306, as "db" host.**

![image](https://github.com/user-attachments/assets/f417dd32-3fb6-4589-8cc1-7c11e4e2890b)


# Pushing the Flask App Image to Docker HUB
 **First create a docker hub account, then log into it to push and follow these commands:** <br/>
 > docker login <br/>
 > docker image tag yourtag username/reponame:imagetag<br/>
 > docker push username/reponame:tag <br/>

 # How to Pull the Image and use it
 1. pull the image
    
    > docker pull 1maya1/training:v1
    
2. Make sure to have docker-compose installed, if not install it using this command
   
   > curl -SL https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
   > chmod +x /usr/local/bin/docker-compose

3. Download the provided Docker-compose.yml file and run the following command

   > docker-compose up
