-- use startersql;

-- gives females with =(equal to)
-- select * from users where gender='Female';

-- gives males and others with <> or !=(not equal to)
-- select * from users where gender!='Female'

-- using < (saller than) to fetch salary
-- select * from users where salary<50000.00;

-- SELECT * FROM users WHERE id <= 5;

-- select * from users where name is null;
-- select * from users where name is not null;

-- select * from users where salary between 50000.00 and 70000.00

-- select * from users where gender in ('Male','Other');

-- select * from users where name like "A%";
-- select * from users where name like "%e";
-- select * from users where name like "%li%"

-- select * from users where gender='Female' and salary>60000.00;
-- select * from users where gender='Male' or gender='Other';

-- select * from users order by salary asc;
-- select * from users order by salary desc;

-- select * from users limit 5;
-- select * from users limit 3 offset 5;
-- select * from users limit 5, 4;
-- select * from users order by salary desc limit 5;

