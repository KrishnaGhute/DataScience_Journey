use startersql;

-- drop table if exists adderss;

-- create table adderss(
-- id int auto_increment primary key,
-- user_id int,
-- street varchar(250),
-- city varchar(100),
-- state varchar(100),
-- pincode varchar(10),
-- constraint fk_user foreign key (user_id) references users(id) on delete cascade
-- );

-- INSERT INTO adderss (user_id, street, city, state, pincode) VALUES
-- (1, '123 Maple St', 'New York', 'NY', '10001'),
-- (2, '456 Oak Ave', 'Los Angeles', 'CA', '90001'),
-- (3, '789 Pine Rd', 'Chicago', 'IL', '60601'),
-- (4, '321 Birch Blvd', 'Houston', 'TX', '77001'),
-- (5, '654 Cedar Ln', 'Phoenix', 'AZ', '85001');

-- View the linked data

-- delete from users where id=3;

select * from users;

SELECT * FROM adderss;