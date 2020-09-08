#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo "THis is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '29i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
