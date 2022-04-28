#!/usr/bin/env bash
# set up web servers if are not already ready

# create dir data if does not exists
mkdir -p data/web_static/releases/test/
mkdir -p data/web_static/shared/

# create example files to test nginx
echo "TEST web static deployment" > data/web_static/releases/test/index.html

# create symbolic link to test folder
sudo ln -sf $PWD/data/web_static/releases/test/ data/web_static/current

# give full ownership of the data directory to ubuntu and group
sudo chown -R ubuntu:ubuntu data

#
# nginx configuration
#

# install servers
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install nginx -y

# redirections - error page
sudo sed -i "s/^server\s{/server {\n\terror_page 404 \/error_simple.html;/1" /etc/nginx/sites-available/default

# configure response header
sudo sed -i "/^server/a \\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default

# replace text: sed syntax is: 's!oldcontent!newcontent!' file.txt
# use s! instead of s/ to avoid having to scape characters
sudo sed -i 's!root /var/www/html;!root /data/web_static/current/;!' /etc/nginx/sites-available/default

# append text: sed syntax is: '/^anothervalue=.*/a after=me' file.txt THIS IS NOT WORKING....
sudo sed -i '/^\tserver_name/ a\\tlocation /hbnb_static \{\n\t\talias /data/web_static/current;\n\t\}\n' /etc/nginx/sites-available/default

### Start service nginx.
sudo service nginx restart
