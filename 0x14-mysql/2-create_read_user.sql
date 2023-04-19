-- Creates the database tyrell_corp and table named nexus6
-- The tyrell_corp has SELECT privilege on nexus6
CREATE DATABASE
    IF NOT EXISTS `tyrell_corp`;

CREATE TABLE
   IF NOT EXISTS `tyrell_corp`.`nexus6` (
   `id`   INT          NOT NULL,
   `name` VARCHAR(256) NOT NULL
);

INSERT INTO
   `tyrell_corp`.`nexus6` (id, name)
   VALUES (1, "Leon");

GRANT SELECT
   ON `tyrell_corp`.*
   TO 'holberton_user'@'localhost';
