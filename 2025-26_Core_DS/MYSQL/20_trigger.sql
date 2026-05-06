use startersql;

-- create table user_log(
-- id int auto_increment primary key,
-- user_id int,
-- name varchar(100),
-- created_on timestamp default current_timestamp
-- );

-- delimiter $$
-- create trigger after_user_insert
-- after insert on users
-- for each row
-- begin
--  INSERT INTO user_log (user_id, name)
--  VALUES (NEW.id, NEW.name);
-- END$$
-- DELIMITER ;

-- INSERT INTO users (name, email, gender, date_of_birth, salary) 
-- VALUES ('Ritika Jain', 'ritika@example.com', 'Female', '1996-03-12', 74000);

-- select * from user_log;
-- select * from users;

-- drop trigger if exists after_user_insert;