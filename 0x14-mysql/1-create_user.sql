-- Creates the user holberton_user with REPLICATION CLIENT privileges.
CREATE USER
    IF NOT EXISTS 'holberton_user'@'localhost'
    IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT
   ON *.*
   TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
