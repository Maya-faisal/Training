# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Install cron
RUN apt-get update && apt-get install -y cron && apt-get install -y bc procps default-mysql-client vim 

RUN pip install mysql-connector-python==8.0.23

# Set the working directory in the container
WORKDIR /flask_blog

# Copy the current directory contents into the container at /app
COPY . /flask_blog

# Add cronjobs scripts
COPY task2.sh task2.sh
COPY avg.sh avg.sh
COPY saveTOdb.py saveTOdb.py
# Make them executable
RUN chmod +x task2.sh avg.sh saveTOdb.py 

# Copy cronjobs config file
COPY crontabs.txt /etc/crontabs/root
COPY bin  bin
RUN crontab /etc/crontabs/root

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
ENV TEMPLATES_AUTO_RELOAD = True
# Copy the startup script into the container
COPY start.sh /start.sh

RUN chmod +x /start.sh

# Run the startup script when the container launches
CMD bash /start.sh ; python3 saveTOdb.py &

