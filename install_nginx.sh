#!/bin/bash

# Update package lists
sudo apt-get update

# Install nginx
sudo apt-get install -y nginx

# Create a new directory to store the application
sudo mkdir /var/www/myapp

# Copy the application code to the new directory
sudo cp -r /path/to/your/app/* /var/www/myapp

# Install the necessary dependencies
sudo pip3 install -r /var/www/myapp/requirements.txt

# Create a new config file for nginx
sudo bash -c 'cat > /etc/nginx/sites-available/myapp <<EOF
server {
    listen 80;
    server_name myapp.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/myapp/myapp.sock;
    }
}
EOF'

# Create a new service file for systemd
sudo bash -c 'cat > /etc/systemd/system/myapp.service <<EOF
[Unit]
Description=myapp

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/myapp
ExecStart=/usr/bin/gunicorn --bind unix:/var/www/myapp/myapp.sock app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF'

# Enable the new service file
sudo systemctl enable myapp

# Start the new service
sudo systemctl start myapp

# Enable the new nginx config
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/

# Test the nginx config
sudo nginx -t

# Reload nginx
sudo systemctl reload nginx

