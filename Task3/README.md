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

# DataBase
**Maria DataBase was used to store the data**

 ![image](https://github.com/user-attachments/assets/4571bef5-6a14-47f9-a707-ddb59a3dbd33)

# Docker and Containerization

**1. First, create the Dockerfile for the Flask App**

>#Use an official Python runtime as a parent image<br/>
>FROM python:3.8-slim-buster<br/>

>#Install cron<br/>
>RUN apt-get update && apt-get install -y cron && apt-get install -y bc procps default-mysql-client<br/>

>#install database connector<br/>
>RUN pip install mysql-connector-python==8.0.23<br/>

>#Set the working directory in the container<br/>
>WORKDIR /flask_blog<br/>

>#Copy the current directory contents into the container at /app<br/>
>COPY . /flask_blog<br/>

>#Add cronjobs scripts<br/>
>COPY task2.sh task2.sh<br/>
>COPY avg.sh avg.sh<br/>

>#Make them executable<br/>
>RUN chmod +x task2.sh avg.sh<br/>

>#Copy cronjobs config file<br/>
>COPY crontabs.txt /etc/crontabs/root<br/>
>RUN crontab /etc/crontabs/root<br/>

>#Install any needed packages specified in requirements.txt<br/>
>RUN pip install --no-cache-dir -r requirements.txt<br/>

>#Make port 5000 available to the world outside this container<br/>
>EXPOSE 5000<br/>

>#Define environment variable<br/>
>ENV FLASK_APP=app.py<br/>
>ENV FLASK_DEBUG=1<br/>

>#Copy the startup script into the container and make it exectabel<br/>
>COPY start.sh /start.sh<br/>
>RUN chmod +x /start.sh<br/>

>#Run the startup script when the container launches<br/>
>CMD ["bash", "/start.sh"]<br/>

**The start.sh script file starts the cronjobs and the flask App**<br/>

>#!/bin/sh<br/>
>#Start the Flask app<br/>
>flask run --host=0.0.0.0 &<br/>
>#Start cron in the foreground<br/>
>cron -f<br/>

**2. Create the docker-compose file**<br/>

Create the compose file that links the app with the database, and pass the database credentials.<br>
It builds the flask app image with tag v1 and host it on port 5000, mariadb image on port 3306, as "db" host.

![image](https://github.com/user-attachments/assets/d7937153-368d-4214-9f8a-7268cbbac613)

   


