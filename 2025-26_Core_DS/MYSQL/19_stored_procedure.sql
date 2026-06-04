use startersql;

-- delimiter $$
-- create procedure select_users()
-- begin
-- 	select *  from users;
-- end $$
-- delimiter ;

-- call select_users()

-- DELIMITER $$
-- CREATE PROCEDURE AddUser(
--  IN p_name VARCHAR(100),
--  IN p_email VARCHAR(100),
--  IN p_gender ENUM('Male', 'Female', 'Other'),
--  IN p_dob DATE,
--  IN p_salary INT
-- )
-- BEGIN
--  INSERT INTO users (name, email, gender, date_of_birth, salary)
--  VALUES (p_name, p_email, p_gender, p_dob, p_salary);
-- END$$
-- DELIMITER ;

-- call AddUser('jwala','jwala@gmail.com','Female','1990-07-21',55000)

-- select * from users;

-- show procedure status where Db='startersql';

-- drop procedure if exists AddUser;
-- drop procedure if exists select_users;