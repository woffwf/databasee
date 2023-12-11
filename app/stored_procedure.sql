DROP TRIGGER IF EXISTS prevent_insert_additional;
DELIMITER //
CREATE TRIGGER prevent_insert_additional
BEFORE INSERT ON additional
FOR EACH ROW
BEGIN
    DECLARE airline_count INT;

    SELECT COUNT(*) INTO airline_count FROM airline WHERE id = NEW.airline_id;

    IF airline_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot insert additional data without a valid airline';
    END IF;
END;
//
DELIMITER ;
DROP PROCEDURE IF EXISTS insert_airline;
DELIMITER //
CREATE PROCEDURE insert_airline(
    IN p_name VARCHAR(45)
)
BEGIN
    DECLARE last_airline_id INT;

    IF NOT (p_name IS NULL) THEN
        INSERT INTO airline (name) VALUES (p_name);
        SET last_airline_id = LAST_INSERT_ID();
        SELECT * FROM airline WHERE id = last_airline_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'All parameters must be provided';
    END IF;
END;//
DELIMITER ;
DROP PROCEDURE IF EXISTS insert_data_procedure
DELIMITER //
CREATE PROCEDURE insert_data_procedure(
    IN way VARCHAR(255),
    IN price INT,
    IN weight INT,
    IN dimensions INT,
    IN date_time DATE,
    IN airline_id INT,
    IN type_of_fly VARCHAR(255),
    IN avaible_seats INT
)
BEGIN
    INSERT INTO available_flights (way, price, time, airline_id, type_of_fly, avaible_seats)
    VALUES (way, price, date_time, airline_id, type_of_fly, avaible_seats);

    SET @table1_id = LAST_INSERT_ID();

    INSERT INTO avaible_weight (mark, person_id) VALUES (weight, dimensions);
    SET @table2_id = LAST_INSERT_ID();

    INSERT INTO film_has_rating (film_id, rating_id) VALUES (@table1_id, @table2_id);
END;//
DELIMITER ;
DROP PROCEDURE IF EXISTS insert_noname_airline;
DELIMITER //
CREATE PROCEDURE insert_noname_airline()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
        INSERT INTO airline (name)
        VALUES (CONCAT('Noname', counter));

        SET counter = counter + 1;
    END WHILE;
    SELECT * FROM airline WHERE name LIKE 'Noname%';
END //
DELIMITER ;
DROP PROCEDURE IF EXISTS get_available_flights_statistics;
DELIMITER //

CREATE PROCEDURE get_available_flights_statistics()
BEGIN
    DECLARE max_avaible_seats DECIMAL(18,2);
    DECLARE min_avaible_seats DECIMAL(18,2);
    DECLARE sum_avaible_seats DECIMAL(18,2);
    DECLARE avg_avaible_seats DECIMAL(18,2);

    SELECT MAX(avaible_seats) INTO max_avaible_seats FROM available_flights;
    SELECT MIN(avaible_seats) INTO min_avaible_seats FROM available_flights;
    SELECT SUM(avaible_seats) INTO sum_avaible_seats FROM available_flights;
    SELECT AVG(avaible_seats) INTO avg_avaible_seats FROM available_flights;

    SELECT 'Max seats:', max_avaible_seats;
    SELECT 'Min seats:', min_avaible_seats;
    SELECT 'Sum seats:', sum_avaible_seats;
    SELECT 'Avg seats:', avg_avaible_seats;
END //
DELIMITER ;
DROP PROCEDURE IF EXISTS create_dynamic_tables;
DELIMITER //

CREATE PROCEDURE create_dynamic_tables()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE table_name_cursor VARCHAR(255);
    DECLARE column_count INT;
    DECLARE column_name VARCHAR(255);

    DECLARE cur_tables CURSOR FOR
        SELECT name, created_at
        FROM table_with_timestamp;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur_tables;

    read_tables: LOOP
        FETCH cur_tables INTO table_name_cursor, column_name;
        IF done THEN
            LEAVE read_tables;
        END IF;

        SET column_count = FLOOR(1 + RAND() * 9);

        SET @sql = CONCAT('CREATE TABLE `', REPLACE(table_name_cursor, ' ', '_'), '_', UNIX_TIMESTAMP(NOW()), '` (');

        SET @column_definitions = '';
        SET @i = 0;

        WHILE @i < column_count DO
            SET @column_name = CONCAT('column', @i);
            SET @column_type = CASE FLOOR(1 + RAND() * 3)
                WHEN 1 THEN 'INT'
                WHEN 2 THEN 'VARCHAR(255)'
                WHEN 3 THEN 'DOUBLE'
            END;

            SET @column_definitions = CONCAT(@column_definitions, @column_name, ' ', @column_type);

            SET @i = @i + 1;
            IF @i < column_count THEN
                SET @column_definitions = CONCAT(@column_definitions, ', ');
            END IF;
        END WHILE;

        SET @sql = CONCAT(@sql, @column_definitions, ');');

        PREPARE stmt FROM @sql;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    CLOSE cur_tables;
END //

DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_double_zeros_airline
BEFORE INSERT ON airline
FOR EACH ROW
BEGIN
    IF NEW.name LIKE '%00' THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Value cannot end with double zeros';
    END IF;
END;
//
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_modification_update_airline
BEFORE UPDATE ON airline
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Modification of data is not allowed';
END;
//
DELIMITER ;
DELIMITER //
CREATE TRIGGER prevent_deletion_airline
BEFORE DELETE ON airline
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Deletion of records is not allowed';
END;
//
DELIMITER ;