-- creates a database called hbtn_0d_usa and a table called states in it
CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_usa`;
USE DATABASE `hbtn_0d_usa`;
CREATE TABLE
	IF NOT EXISTS `states`(PRIMARY KEY(`id`),`id` INT AUTO_INCREMENT, `name` VARCHAR(256));
