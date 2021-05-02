#!/usr/bin/env bash
# a comment

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "with simple content, to test your Nginx configuration" | sudo tee /data/web_static/releases/test/index.html
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0

