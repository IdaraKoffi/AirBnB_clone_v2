#!/usr/bin/env bash
# A bash script to set up web servers for deployment of web_static

# Install Nginx if it's not already installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create required directories if they don't exist
directories=("/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test")
for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        sudo mkdir -p "$dir"
    fi
done

# Create a fake HTML file
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -L "/data/web_static/current" ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_text="
location /hbnb_static {
    alias /data/web_static/current/;
}
"
# Use double quotes and escape $ and \ to prevent variable interpolation
sudo sed -i -e "/server_name _;/a $config_text" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
