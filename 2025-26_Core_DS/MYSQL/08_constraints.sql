use startersql;

-- 01.unique
-- alter table users add constraint unique_email unique(email);
-- insert into users values ('Alice', 'alice@example.com', 'Female', '1992-03-12', 55000.00);

-- 02.not null
-- alter table users modify column name varchar(100) not null;
-- insert into users values (null, 'alice@example.com', 'Female', '1992-03-12', 55000.00);

-- 03.check constraint
-- alter table users add constraint chk_dob check (date_of_birth>'1985-01-01');
-- insert into users values ('kusa', 'kusa@example.com', 'Female', '1983-03-12', 55000.00);

-- 04.DEFAULT
-- Sets a default value

-- 05.PRIMARY KEY 
-- Uniquely identifies each row

-- 06.AUTO_INCREMENT 
-- Automatically generates unique numbers

select * from users;