#!/usr/bin/env bash
# set up web servers if are not already ready

# install servers
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo apt-get autoremove -y

# create dir data if does not exists
mkdir -p data/web_static/releases/test/
mkdir -p data/web_static/shared/

# create symbolic link to test folder
sudo ln -sf $PWD/data/web_static/releases/test/ data/web_static/current

# give full ownership of the data directory to ubuntu and group
sudo chown -R ubuntu:ubuntu data *

# create example files to test nginx
echo "FINALY!!! Testing nginx automatic conf." > $PWD/data/web_static/releases/test/index.html

#
# nginx configuration
#

# redirections - error page
sudo sed -i "s/^server\s{/server {\n\terror_page 404 \/error_simple.html;/1" /etc/nginx/sites-available/default

# configure response header
sudo sed -i "/^server/a \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default

# append text: sed syntax is: '/^anothervalue=.*/a after=me' file.txt THIS IS NOT WORKING....
sudo sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default

### Start service nginx.
sudo service nginx restart
