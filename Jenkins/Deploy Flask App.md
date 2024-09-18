# Deploying Flask App using Jenkins and Docker

This repository demonstrates how to deploy a Flask application and a MariaDB container using Jenkins and Docker. The pipeline will automate the deployment process, ensuring that both the Flask app and the database are correctly set up and linked.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Setup Instructions](#setup-instructions)
- [Pipeline Details](#pipeline-details)
- [Environment Variables](#environment-variables)
- [Docker Images](#docker-images)
- [Cleanup](#cleanup)
- [Future Enhancements](#future-enhancements)

---

## Prerequisites

Before using this repository, make sure you have the following installed:

1. **Jenkins** - Installed on your CentOS 9 VM or a compatible environment.
2. **Docker** - Installed and running. Jenkins must be able to execute Docker commands.
3. **Git** - To clone this repository and track changes.
4. **Flask Application Docker Image** - A prebuilt Docker image of the Flask app.
5. **MariaDB Docker Image** - The official MariaDB image pulled from Docker Hub.

---

## Architecture

This project consists of the following components:
- **Flask App Container**: A Python-based web application built using Flask.
- **MariaDB Container**: A relational database used by the Flask app for data storage.

The Jenkins pipeline pulls both images from Docker Hub (or a private registry), runs the MariaDB container, and then runs the Flask container linked to the database.

---

## Jenkins Pipeline

The Jenkins pipeline script is located in the [Jenkinsfile](./Jenkinsfile) and includes the following stages:
1. **Pull Flask App and MariaDB**: Fetches the latest versions of both images.
2. **Run MariaDB Container**: Starts the MariaDB container with necessary environment variables.
3. **Run Flask App Container**: Runs the Flask app container, linking it to the MariaDB container.
4. **Cleanup**: Removes both containers after the pipeline completes.

---

## Setup Instructions

Follow these steps to deploy the Flask app using Jenkins:

1. **Install Jenkins** on your CentOS 9 VM:
   
   ```bash
   sudo dnf install java-11-openjdk
   sudo dnf install jenkins
   sudo systemctl start jenkins
   sudo systemctl enable jenkins

2. Install Docker and add Jenkins to the Docker group:

   ```bash
   sudo dnf install docker
   sudo systemctl start docker
   sudo usermod -aG docker jenkins
   sudo systemctl restart jenkins

3. Configure Jenkins:

   Install the Docker Pipeline plugin.
   Create a new pipeline project in Jenkins.
   In the project configuration, set the pipeline to use the Jenkinsfile from this repository.

4. Run the pipeline:

   Trigger a build in Jenkins, and the pipeline will pull the Docker images and run the containers.


  

