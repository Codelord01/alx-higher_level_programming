-- list all not null name records
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != NULL
ORDER BY `score` DESC;
