use startersql;

-- select avg(salary) from users;

-- select * from users where salary > (select avg(salary) from users);

-- select id, name, reffer_by_id
-- from users 
-- where reffer_by_id in(
-- select id from users where salary > (select avg(salary) from users)
-- );