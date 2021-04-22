select * from users limit 10;

update users set updated_at = now() where created_at > users.updated_at;

desc profiles;

select * from profiles limit 10;

update profiles set gender = 'f' where gender = 'w';


update profiles set updated_at = now() where created_at > updated_at;



desc messages;

select * from messages limit 10;

-- update messages set from_user_id = floor(1 + rand() * 100);

desc media;

update media set updated_at = now() where created_at > updated_at;

select * from media limit 10;

-- http://dropbox.net/vk/filename.ext

create temporary table extensions (name VARCHAR(10));

insert into extensions values ('jpeg'), ('mp3'), ('mp4'), ('avi');
select * from extensions;

select name from extensions order by rand() limit 1;

update media set filename = concat(
    'http://dropbox.net/vk/',
    filename,
    '.',
    (select name from extensions order by rand() limit 1));

update media set size = floor(10000 + rand() * 100000000) where size < 15000;

-- '{"owner":"user_id" }'

update media set metadata = concat(
    '{"owner":"',
    (select concat(first_name, ' ', last_name) from users where id = user_id),
    '"}');
select concat(first_name, ' ', last_name) from users where id = 4;



select * from media_types;

delete from media_types;

insert into media_types (name) values
    ('photo'),
    ('audio'),
    ('video');

update media_types set name = 'games' where id =4;

update media_types set updated_at = now() where created_at > updated_at;


select * from media where media_type_id > 4;

alter table media modify column metadata JSON;

desc profiles;

alter table profiles modify column gender ENUM('m', 'f');


select * from profiles limit 10;

desc friendship;

update friendship set updated_at = now() where created_at > updated_at;


-- alter table friendship drop column reques


select * from friendship;

desc friendship_statuses;

select * from friendship_statuses;

update friendship_statuses set name = 'Rejected' where id = 3;

select * from friendship;

update friendship set confirmed_at = now() where confirmed_at < friendship.created_at


desc communities;


select * from communities

update communities set updated_at = now() where created_at > updated_at;

select * from communities_users;

truncate communities_users;

desc communities_users;
insert into communities_users
select floor(1 + RAND() * 7), floor(1 + RAND() * 100), now()
from users limit 50;


-- select floor(1 + RAND() * 7), floor(1 + RAND() * 100), now();

-- select floor(1 + RAND() * 7), floor(1 + RAND() * 7) from messages limit 100;



