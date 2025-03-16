
-------------- check version first ---------------------------
apt-cache show mariadb-server | grep Version
--------------------------------------------------------------
sudo apt-get install apt-transport-https curl
sudo mkdir -p /etc/apt/keyrings
sudo curl -o /etc/apt/keyrings/mariadb-keyring.pgp 'https://mariadb.org/mariadb_release_signing_key.pgp'


create a file 

--------------------------------------------
/etc/apt/sources.list.d/mariadb.list
--------------------------------------------

---------------------- copy and paste the script below to the above created file mariadb.list ------------------
# MariaDB 11.8 repository list - created 2025-03-14 15:24 UTC
# https://mariadb.org/download/
# deb.mariadb.org is a dynamic mirror if your preferred mirror goes offline. See https://mariadb.org/mirrorbits/ for details.
# deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://deb.mariadb.org/11.8/ubuntu noble main
deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://ftp.ubuntu-tw.org/mirror/mariadb/repo/11.8/ubuntu noble main
# deb-src [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://ftp.ubuntu-tw.org/mirror/mariadb/repo/11.8/ubuntu noble main
---------------------------------------------------------------------------------------------------------------------------------

------------------ check version again
apt-cache show mariadb-server | grep Version
--------------------------------------------

sudo apt install mariadb-server=1:11.8.1+maria~ubu2404

------------------- after installation start mariadb -----------------
sudo service mariadb start or sudo systemctl start mariadb   
---------------------------------------------------------------------
------------------------ secure installation 
sudo mysql_secure_installation or mariadb-secure-installation  -> options for answer [ n,n,y,n,y,y]
---------------------------------------------

sudo mariadb -u root -p



1. CREATE DATABASE default_db1;
2. CREATE USER 'default'@'%' IDENTIFIED BY '1234';
3. GRANT ALL PRIVILEGES ON default_db1.* TO 'default'@'%';
4. FLUSH PRIVILEGES;
5. SHOW GRANTS FOR 'default'@'%';


---------------------- let the django connect to this ---------------------------
sudo apt-get install pkg-config
sudo apt-get install libmariadb-dev libmariadb-dev-compat

------------------------------------------------------------------------------------

pip install mysqlclient
