# Deploying Flask App using Jenkins and Docker

This repository demonstrates how to deploy a Flask application and a MariaDB container using Jenkins and Docker. The pipeline will automate the deployment process, ensuring that both the Flask app and the database are correctly set up and linked.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Architecture](#architecture)
- [Docker Compose Setup](#docker-compose-setup)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Setup Instructions](#setup-instructions)
- [Pipeline Details](#pipeline-details)
- [Environment Variables](#environment-variables)
- [Cleanup](#cleanup)
- [Future Enhancements](#future-enhancements)

---

## Prerequisites

Before using this repository, make sure you have the following installed:

1. **Jenkins** - Installed on your CentOS 9 VM or a compatible environment.
2. **Docker** - Installed and running. Jenkins must be able to execute Docker commands.
3. **Git** - To clone this repository and track changes.
4. **Docker Compose** - Installed and configured for container orchestration.
5. **Flask Application** - Dockerized and ready to be built from the `Dockerfile`.

---

## Architecture

This project consists of the following components:
- **Flask App Container**: A Python-based web application built using Flask.
- **MariaDB Container**: A relational database used by the Flask app for data storage.

The deployment is handled via Docker Compose, which runs both containers and manages their lifecycle and networking.

---
## Docker Compose Setup

This project uses Docker Compose to orchestrate the deployment. The `docker-compose.yml` file is located in task3 directory.

---

## Jenkins Pipeline

The Jenkins pipeline script uses Docker Compose to start the services. It pulls the necessary images and builds the Flask app, and then Docker Compose manages the deployment.

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
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.6.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   sudo systemctl start docker
   sudo usermod -aG docker jenkins
   sudo systemctl restart jenkins


3. Configure Jenkins:

   Install the Docker Pipeline plugin.
   Create a new pipeline project in Jenkins.
   In the project configuration, set the pipeline to use the Jenkinsfile from this repository.

4. Run the pipeline:

   Trigger a build in Jenkins, and the pipeline will pull the Docker images and run the containers.

---
## Pipeline Details
The Jenkinsfile contains the following stages:
```bash
   pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Build and Run Containers') {
            steps {
                script {
                    // Build and run the containers using Docker Compose
                    sh 'docker-compose up -d --build'
                }
            }
        }
    }
    post {
        always {
            script {
                // Clean up containers after pipeline completes
                sh 'docker-compose down'
            }
        }
    }
 }
```
**Key Components**:
Checkout Code: Pulls the latest version of the code from the GitHub repository.
Docker Compose Up: Builds and runs the services (MariaDB and Flask app) in detached mode (-d).
Cleanup: Stops and removes the containers after the pipeline completes.

---
## Environment Variables
The following environment variables are used in the docker-compose.yml file:

MARIADB_ROOT_PASSWORD: The root password for the MariaDB container. <br/>
MARIADB_DATABASE: The name of the database created for the Flask app. <br/>
MARIADB_USER: The user with privileges to the database. <br/>
MARIADB_PASSWORD: The password for the specified database user. </br>

These environment variables can be modified as needed in the docker-compose.yml file. </br>

---
## Cleanup
After the pipeline finishes, Docker Compose will stop and remove the containers. You can also manually stop and remove the containers using the following command:

```bash
   docker-compose down
```
This will stop the running containers and remove them from the system.

---
## Future Enhancements
- Automated Testing: Add a test stage to run unit tests for the Flask app before deployment.
- Persistent Data: The MariaDB service uses a persistent volume (db_data) to store database data across runs.
- CI/CD: Integrate GitHub webhooks to automatically trigger Jenkins builds when code is pushed to the repository.
