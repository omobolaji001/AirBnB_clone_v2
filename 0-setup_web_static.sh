#!/usr/bin/env bash
# a scripts that sets up the web server for deployment of web_static

# installs nginx
apt-get update
apt-get -y install nginx

# creates folder /data
mkdir -p /data/

# creates folder /data/web_static
mkdir -p /data/web_static/

# creates folder /data/web_static/releases
mkdir -p /data/web_static/releases/

# creates folder /data/web_static/shared
mkdir -p /data/web_static/shared/

# creates folder /data/web_static/releases/test/
mkdir -p /data/web_static/releases/test/

# creates a fake HTML file with content
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# creates a symbolink link /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

# gives ownership of /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Nginx configuration
sed -i '/listen 80 default/a\ \tlocation /hbnb_static { \n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# restarts nginx
service nginx restart

