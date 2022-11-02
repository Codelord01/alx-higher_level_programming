-- creates a database and adds a user with only SELECT privilege
CREATE IF NOT EXISTS DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS
`user_0d_2`@`localhost`
IDENTIFIED BY `user_0d_2_pwd`;
GRANT SELECT
ON `hbtn_0d_2`
TO `user_0d_2`@`localhost`;
