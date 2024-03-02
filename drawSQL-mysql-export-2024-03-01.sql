CREATE TABLE `user`(
    `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(255) NOT NULL,
    `password` VARCHAR(255) NOT NULL,
    `full_name` VARCHAR(255) NULL,
    `email` VARCHAR(255) NULL,
    `status` TINYINT(1) NULL,
    `img` VARCHAR(255) NULL,
    `role_id` INT NOT NULL
);
CREATE TABLE `message`(
    `qa_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `session_id` INT NOT NULL,
    `question` TEXT NOT NULL,
    `answer` TEXT NOT NULL,
    `question_time` DATETIME NOT NULL,
    `answer_time` DATETIME NOT NULL,
    `comment` TEXT NULL
);
CREATE TABLE `session`(
    `session_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` TEXT NULL,
    `start_time` DATETIME NOT NULL,
    `end_time` DATETIME NULL,
    `user_id` INT NOT NULL
);
CREATE TABLE `role`(
    `role_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `role_name` VARCHAR(255) NOT NULL
);
CREATE TABLE `information`(
    `in_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `link` TEXT NOT NULL
);
ALTER TABLE
    `user` ADD CONSTRAINT `user_role_id_foreign` FOREIGN KEY(`role_id`) REFERENCES `role`(`role_id`);
ALTER TABLE
    `session` ADD CONSTRAINT `session_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `message` ADD CONSTRAINT `message_session_id_foreign` FOREIGN KEY(`session_id`) REFERENCES `session`(`session_id`);