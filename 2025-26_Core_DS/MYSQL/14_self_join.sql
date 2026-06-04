use startersql;

-- s1 . adding reffer_by_id column
-- alter table users
-- add column reffer_by_id int;

-- s2 . inserting referal data
-- update users set reffer_by_id=1 where id in (2,3,8);
-- update users set reffer_by_id=2 where id in (6,7);

-- s3 . use self join to get reffered names
-- select
-- a.id,
-- a.name as user_name,
-- b.name as reffered_by
-- from users a
-- inner join users b on a.reffer_by_id=b.id;

-- select * from users;