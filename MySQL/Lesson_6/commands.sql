use vk;

DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  target_id INT UNSIGNED NOT NULL,
  target_type ENUM('messages', 'users', 'posts', 'media') NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS target_types;
CREATE TEMPORARY TABLE target_types (
  name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO target_types (name) VALUES
  ('messages'),
  ('users'),
  ('media'),
  ('posts');

INSERT INTO likes
  SELECT
    id,
    FLOOR(1 + (RAND() * 100)),
    FLOOR(1 + (RAND() * 100)),
    (SELECT name FROM target_types ORDER BY RAND() LIMIT 1),
    CURRENT_TIMESTAMP
  FROM messages;

DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  community_id INT UNSIGNED,
  head VARCHAR(255),
  body TEXT NOT NULL,
  media_id INT UNSIGNED,
  is_public BOOLEAN DEFAULT TRUE,
  is_archived BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

ALTER TABLE profiles
    ADD CONSTRAINT profiles_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE;

ALTER TABLE messages
    ADD CONSTRAINT messages_from_user_id_fk
        FOREIGN KEY (from_user_id) REFERENCES users(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT messages_to_user_id_fk
        FOREIGN KEY (to_user_id) REFERENCES users(id)
            ON DELETE CASCADE;

ALTER TABLE media
    ADD CONSTRAINT media_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT media_type_id_fk
        FOREIGN KEY (media_type_id) REFERENCES media_types(id)
            ON DELETE CASCADE;

ALTER TABLE posts
    ADD CONSTRAINT posts_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT posts_community_id_fk
        FOREIGN KEY (community_id) REFERENCES communities(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT posts_media_id_fk
        FOREIGN KEY (media_id) REFERENCES media(id)
            ON DELETE CASCADE;

ALTER TABLE communities_users
    ADD CONSTRAINT communities_users_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT communities_users_community_id_fk
        FOREIGN KEY (community_id) REFERENCES communities(id)
            ON DELETE CASCADE;

ALTER TABLE likes
    ADD CONSTRAINT likes_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE;

ALTER TABLE friendship
    ADD CONSTRAINT friendship_user_id_fk
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT friendship_friend_id_fk
        FOREIGN KEY (friend_id) REFERENCES users(id)
            ON DELETE CASCADE,
    ADD CONSTRAINT friendship_friendship_status_id_fk
        FOREIGN KEY (friendship_status_id) REFERENCES friendship_statuses(id)
            ON DELETE CASCADE;

-- Кто больше поставил лайков
SELECT count(user_id) as count_likes, 'M' as sex
FROM likes
WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'm')
UNION ALL
SELECT count(user_id), 'F'
FROM likes
WHERE user_id IN (SELECT user_id FROM profiles WHERE gender = 'f')
ORDER BY count_likes DESC
LIMIT 1;

-- Сколько лайков получили 10 самых молодых пользователей
SELECT SUM(count_likes) as RESULT_COUNT FROM
    (SELECT COUNT(*) as count_likes
               FROM likes AS likes
                    LEFT JOIN profiles AS prof ON likes.target_id = prof.user_id
               WHERE target_type = 'users'
               GROUP BY target_id, birthday
               ORDER BY birthday DESC
               LIMIT 10
              ) AS COUNT;

-- 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети

SELECT id, SUM(active) as total_activity from
(SELECT user_id as id, 1 as active from friendship
UNION ALL
SELECT user_id, 1 from likes
UNION ALL
SELECT user_id, 1 from media
UNION ALL
SELECT from_user_id, 1 from messages
UNION ALL
SELECT user_id, 1 from posts
UNION ALL
SELECT id, 0 FROM users) as activity
GROUP BY id
ORDER BY total_activity
LIMIT 10;







