use startersql;

-- update users set name='guru' where id=1;
-- update users set name='guru' , email='guru@example.com' where id=1;

-- update users set salary=60000.00 where id=5;

-- set sql_safe_updates=0;
-- update users set salary = salary + 5000 where salary<60000;
-- set sql_safe_updates=1;

-- update users set salary = salary + 5000 where salary<60000 and id>0;

select * from users;