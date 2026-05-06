use startersql;

-- select gender, avg(salary) as "average salary" from users group by gender;

-- select gender as "Gender", avg(salary) as "Average salary", count(*) as "Count"
-- from users where id < 40
-- group by gender
-- having avg(salary) > 60000;

-- select reffer_by_id, count(*) as total_refferels
-- from users
-- where reffer_by_id is not null
-- group by reffer_by_id
-- having count(*) > 1;

select gender as "Gender", avg(salary) as "Average salary", count(*) as "Count"
from users where id < 40
group by gender
with rollup
having avg(salary) < 60000;