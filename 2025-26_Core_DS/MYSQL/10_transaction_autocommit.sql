use startersql;

-- 01.disabiling autocommit
-- set autocommit = 0;

-- by mistek
-- delete from users where id=5;

-- taking commit back
-- rollback;

-- now deleting the 6th id
-- delete from users where id=6;

-- for final commit
-- commit;

-- activating autocommit
-- set autocommit=1;
select * from users;