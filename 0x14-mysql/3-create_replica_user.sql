-- Creates the user replica_user with REPLICATION SLAVE privileges.
-- Grant read previvilages on mysql.user table to holberton_user.
CREATE USER
    IF NOT EXISTS 'replica_user'@'%'
    IDENTIFIED BY 'replica_user123';

GRANT REPLICATION SLAVE
   ON *.*
   TO 'replica_user'@'%';

FLUSH PRIVILEGES;

GRANT SELECT
   ON `mysql`.`user`
   TO 'holberton_user'@'localhost';
