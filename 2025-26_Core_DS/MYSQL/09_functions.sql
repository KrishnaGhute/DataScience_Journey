use startersql;

-- 01.aggregate function : returns only single value

-- count()
-- select count(*) from users;
-- select count(*) from users where gender='Female';

-- min() and max()
-- select min(salary) as min_sal, max(salary) as max_sal from users;

-- sum()
-- select sum(salary) as total_sal from users;
-- select sum(salary) as femal_sal from users where gender='Female';

-- avg()
-- select avg(salary) as total_sal from users;
-- select avg(salary) as femal_sal from users where gender='Female';

-- grouping 
-- select gender, avg(salary) as avg_sal from users group by gender;
-- select gender, sum(salary) as avg_sal from users group by gender;

-- 02.string function

-- length()
-- select name, length(name) as name_length from users;

-- lower() and upper()
-- select name, lower(name) as lower_name, upper(name) as upper_name from users;

-- concat()
-- select name,concat(name,'5094') as user_name from users;

-- 03.date function

-- now()
-- select now()
-- select name, now() from users;

-- year(), month(), day()
-- select name, year(date_of_birth) as birth_year from users;

-- datediff()
-- select name, datediff(curdate(), date_of_birth) as days_lived from users;

-- timestampdiff()
-- select name, timestampdiff(year, date_of_birth, curdate()) as age from users;

-- 04.mathematicla function

-- round(), floor(), ceil()
-- select salary, round(salary) as rounded, floor(salary) as floored, ceil(salary) as ceiled from users;

-- mod()
-- select id,mod(id,2) as remainder from users;

-- 05.conditional functions

-- if()
-- select name, gender, if(gender='Female','yes','no') as is_female from users;
