
-- Тема Операции, задание 1
-- Пусть в таблице users поля created_at и updated_at оказались незаполненными.
-- Заполните их текущими датой и временем.
UPDATE users
SET created_at = NOW(),
    updated_at = NOW()
WHERE created_at IS NULL
   OR updated_at IS NULL;

-- Тема Операции, задание 2
-- Таблица users была неудачно спроектирована.
-- Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались
-- значения в формате "20.10.2017 8:10".
-- Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.

ALTER TABLE users
    ADD created_at_dt DATETIME;
ALTER TABLE users
    ADD updated_at_dt DATETIME;

UPDATE users
SET created_at_dt = STR_TO_DATE(created_at, '%d.%m.%Y %H:%i'),
    updated_at_dt = STR_TO_DATE(updated_at, '%d.%m.%Y %H:%i');

ALTER TABLE users
    DROP created_at, DROP updated_at,
    RENAME COLUMN created_at_dt TO created_at, RENAME COLUMN updated_at_dt TO updated_at;


-- Тема Операции, задание 3
-- В таблице складских запасов storehouses_products в поле value могут встречаться самые
-- разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы.
-- Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения
-- значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.

SELECT *
FROM storehouses_products
ORDER BY
    IF(value > 0, 0, 1), value;

-- Тема Операции, задание 4
-- (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в
-- августе и мае. Месяцы заданы в виде списка английских названий ('may', 'august')

SELECT
    name,
    IF(
        MONTH(birthday_at) = 5,
        'may',
        'august'
        ) AS birthday_month
FROM users
where MONTH(birthday_at) = 5
   OR MONTH(birthday_at) = 8
