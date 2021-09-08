CREATE TABLE `test_db`.`sales_table` (
  `sales_id` INT NOT NULL,
  `department_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `card_name` VARCHAR(45) NOT NULL,
  `card_number` VARCHAR(45) NOT NULL,
  `transaction_date`  NOT NULL,
  PRIMARY KEY (`sales_id`))