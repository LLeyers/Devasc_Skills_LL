#!/bin/bash

# Install Java
sudo apt-get update
sudo apt-get install -y default-jdk

# Download Jenkins WAR file
wget http://mirrors.jenkins.io/war-stable/latest/jenkins.war

# Start Jenkins as a background process
java -jar jenkins.war --httpPort=8080 --daemon

# Wait for Jenkins to start (you may adjust the sleep time based on your system)
sleep 30

# Print the initial admin password to the console
echo "Initial Admin Password:"
cat ~/.jenkins/secrets/initialAdminPassword
