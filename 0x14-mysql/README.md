# 0x14. MySQL

## Resources

* [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
* [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
* [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

## How to Install mysql 5.7

Copy the key [here](https://dev.mysql.com/doc/refman/5.7/en/checking-gpg-signature.html) to your clipboard.

Save it in a file on your machine i.e. signature.key and then

    sudo apt-key add signature.key

add the apt repo

    sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

update apt

    sudo apt-get update

now check your available versions:

    sudo apt-cache policy mysql-server

Now install mysql 5.7

    sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

## Learning Objectives

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works
