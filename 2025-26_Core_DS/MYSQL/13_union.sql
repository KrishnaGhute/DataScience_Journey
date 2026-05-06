use startersql;

-- CREATE TABLE admin_users (
-- id INT PRIMARY KEY,
--  name VARCHAR(100),
--  email VARCHAR(100),
--  gender ENUM('Male', 'Female', 'Other'),
--  date_of_birth DATE,
--  salary INT
-- );

-- INSERT INTO admin_users (id, name, email, gender, date_of_birth, salary) VALUES
-- (101, 'Anil Kumar', 'anil@example.com', 'Male', '1985-04-12', 60000),
-- (102, 'Pooja Sharma', 'pooja@example.com', 'Female', '1992-09-20', 58000),
-- (103, 'Rakesh Yadav', 'rakesh@example.com', 'Male', '1989-11-05', 54000),
-- (104, 'Fatima Begum', 'fatima@example.com', 'Female', '1990-06-30', 62000);

-- select name from users
-- union        -- gives combine table without repating any simillar row
-- select name from admin_users;

-- select name, email, salary from users
-- union all      -- gives combine table whit repeated rows
-- select name, email, salary from admin_users;


-- select name, email, 'user' as role from users
-- union
-- select name, email, 'admin' as role from admin_users;

-- select name, email, salary from users
-- union
-- select name, email, salary from admin_users
-- order by salary;