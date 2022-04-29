#!/usr/bin/env bash
# set up web servers if are not already ready

# install servers
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y

# create dir data if does not exists
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# create symbolic link to test folder
sudo ln -fs /data/web_static/releases/test /data/web_static/current

# create example files to test nginx
echo """
<html>
    <head>
    </head>
    <body>
        <h1>Holberton School</h1>
    <\body>
</html>
""" | sudo tee /data/web_static/releases/test/index.html

# give full ownership of the data directory to ubuntu and group
sudo chown -hR ubuntu:ubuntu /data/

# redirections - error page
sudo sed -i "s/^server\s{/server {\n\terror_page 404 \/error_simple.html;/1" /etc/nginx/sites-available/default

# configure response header
sudo sed -i "/^server/a \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default

# append text: sed syntax is: '/^anothervalue=.*/a after=me' file.txt THIS IS NOT WORKING....
sudo sed -i '/^\tlisten 80 default_server;/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default

### Start service nginx.
sudo service nginx restart
