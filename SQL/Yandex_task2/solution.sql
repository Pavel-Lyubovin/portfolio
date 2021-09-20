# ПЛАН РЕШЕНИЯ:
# 1. Определить задачи, которые в принципе можно перенести другому исполнителю (по условиям задачи)
# 2. Найти исполнителя - донора, у которого больше всего задач, и есть задачи, которые можно перенести
# 3. Найти исполнителя - реципиента (получателя), у которого меньше всего задач.
# 4. Если разница в общем количестве задач между донором и реципиентом более 1, то осуществить перенос одной задачи от донора к реципиенту
# 5. Повторить п. 2-4 до тех пор, пока разница между количеством задач донора и реципиента не станет 0 или 1
# ----------------------------

# ПОЯСНЕНИЯ:
# Решение тестировалось на mySQL
# Сделал решение полностью на SQL в том числе и ввод входных параметров
# - так легче проверить задание.
# В реальном проекте я бы так делать не стал и часть операций перенес бы на бэкенд.
# Временные таблицы нельзя использовать дважды в одном запросе (по крайней мере, в mySQL).
# Т.к. я использовал временную таблицу assigneeList (с входными параметрами),
# то мне также пришлось делать временные таблицы `load_tasks`, `move_tasks`,
# `work_situation` и т.д. чтобы обойти ограничение на двойное использование assigneeList
# В реальном проекте я бы использовал более сложные запросы и джойнил бы st_task саму с собой.
# Но зато с временными таблицами получилось более понятное решение )).


#---------------------------------------
# Инициализация входных параметров:
# @days and `assigneeList`

SET @days = 5;

DROP TABLE IF EXISTS `assigneeList`;
CREATE TEMPORARY TABLE `assigneeList`
(`assignee` int);
# Заполнение assigneeList. VALUES(1), (2), (3) эквивалентно $assigneeList = [1, 2, 3]
INSERT INTO assigneeList VALUES(1), (2), (3);
#---------------------------------------

# Переменная-флаг, которая показывает, можно ли перенести какую-нибудь задачу или нет
SET @cycling = 1;

DELIMITER //

# Основная процедура
DROP PROCEDURE IF EXISTS process_tasks;
CREATE PROCEDURE process_tasks()
BEGIN
# Основной цикл, в котором задачи переносятся по одной штуке
WHILE @cycling DO
	
	# Общая нагрузка
	DROP TABLE IF EXISTS `load_tasks`;
	CREATE TEMPORARY TABLE `load_tasks`
	(
		SELECT assignee, SUM(1) AS load_tasks FROM st_task
			WHERE assignee IN (SELECT assignee FROM assigneeList)
				AND status IN ('Open', 'On support side', 'Verifying')
			GROUP BY assignee
	);
	
	# Нагрузка, которую можно перераспределить
	DROP TABLE IF EXISTS `move_tasks`;
	CREATE TEMPORARY TABLE `move_tasks`
	(
		SELECT assignee, SUM(1) AS move_tasks FROM st_task
			WHERE assignee IN (SELECT assignee FROM assigneeList)
				AND status IN ('Open', 'On support side', 'Verifying')
				AND TIMESTAMPDIFF(day, updated, NOW()) >= @days
			GROUP BY assignee
	);
	
	# Основная рабочая таблица, отражающая ситуацию с нагрузкой в целом
	DROP TABLE IF EXISTS `work_situation`;
	CREATE TEMPORARY TABLE `work_situation`
	(
		SELECT assignee, IFNULL(load_tasks, 0) AS load_tasks, IFNULL(move_tasks, 0) AS move_tasks FROM
			(SELECT * FROM assigneeList) AS a
		LEFT JOIN
			(SELECT * FROM load_tasks) as l USING(assignee)
		LEFT JOIN
			(SELECT * FROM move_tasks) as m USING(assignee)
	);

	# Потенциальный донор, который отдаст свою задачу
	DROP TABLE IF EXISTS `donor`;
	CREATE TEMPORARY TABLE `donor`
	(
	SELECT assignee AS d_assignee, load_tasks AS d_load_tasks, move_tasks AS d_move_tasks
		FROM work_situation
		WHERE move_tasks > 0
		ORDER BY load_tasks DESC LIMIT 1
	);

	# Потенциальный реципиент, который получит задачу от донора
	DROP TABLE IF EXISTS `recipient`;
	CREATE TEMPORARY TABLE `recipient`
	(
	SELECT assignee AS r_assignee, load_tasks AS r_load_tasks, move_tasks AS r_move_tasks
		FROM work_situation
		ORDER BY load_tasks LIMIT 1
	);
	
	# Булева переменная, которая сообщает, состоится ли перенос задачи
	SET @need_move = (SELECT (d_load_tasks - r_load_tasks) > 1 AND d_assignee != r_assignee
	    FROM donor, recipient LIMIT 1);
	
    IF @need_move THEN
    	# Подготовка к переносу
	SET @d_assignee = (SELECT d_assignee FROM donor LIMIT 1);
        SET @r_assignee = (SELECT r_assignee FROM recipient);
        SET @key = (SELECT `key` FROM st_task
            WHERE assignee = @d_assignee
				AND status IN ('Open', 'On support side', 'Verifying')
				AND TIMESTAMPDIFF(day, updated, NOW()) >= @days
                LIMIT 1);
	# Собственно перенос задачи
        UPDATE st_task SET assignee = @r_assignee WHERE `key` = @key;

    ELSE
    	# Завершаю основной цикл
        SET @cycling = 0;
    END IF;
  
	
END WHILE;
END //

CALL process_tasks();
