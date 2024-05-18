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
    `comment` TEXT NULL,
    `star` INT NULL,
    `message_summary` VARCHAR(255) NULL
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
CREATE TABLE `chat_with_emloyee`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `messenger` VARCHAR(255) NOT NULL,
    `emloyee` TINYINT(1) NOT NULL,
    `status` TINYINT(1) NOT NULL,
    `datetime` DATETIME NOT NULL,
    `user_id` INT NOT NULL
);
CREATE TABLE `information`(
    `in_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL,
    `link` TEXT NOT NULL
);

CREATE TABLE `data_score`(
    `id_score` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_career` VARCHAR(255) NOT NULL,
    `score` DOUBLE NOT NULL,
    `name` VARCHAR(255) NOT NULL,
    `id_faculty` INT NULL,
    `year` INT NOT NULL,
    `multiplier` VARCHAR(255) NULL
);
CREATE TABLE `faculty`(
    `id_faculty` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `admission_subject`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_subject` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NULL
);

CREATE TABLE `data_score_vs_subject_combination`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_score` INT NOT NULL,
    `id_combination` VARCHAR(255) NULL,
    `formula` VARCHAR(255) NULL
);

CREATE TABLE `subject_combination_vs_admission_subject`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_combination` VARCHAR(255) NOT NULL,
    `id_subject` VARCHAR(255) NOT NULL
);

CREATE TABLE `subject_combination`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_combination` VARCHAR(255) NOT NULL,
    `name` VARCHAR(255) NULL
);

CREATE TABLE `new_page`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` INT NULL,
    `name` VARCHAR(255) NOT NULL,
    `content` TEXT NOT NULL,
    `create_time` DATETIME NOT NULL,
    `update_time` DATETIME NULL
);

CREATE TABLE `bug_comment`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `bug_question_id` INT NOT NULL,
    `content` TEXT NOT NULL,
    `user_id` INT NOT NULL,
    `user_id_last_comment` INT NOT NULL
);

CREATE TABLE `bug_question`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(255) NOT NULL,
    `content` TEXT NOT NULL,
    `view` INT NOT NULL,
    `create_time` DATETIME NOT NULL,
    `user_id` INT NOT NULL
);

ALTER TABLE
    `chat_with_emloyee` ADD CONSTRAINT `chat_with_emloyee_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `data_score` ADD CONSTRAINT `data_score_id_faculty_foreign` FOREIGN KEY(`id_faculty`) REFERENCES `faculty`(`id_faculty`);
ALTER TABLE
    `user` ADD CONSTRAINT `user_role_id_foreign` FOREIGN KEY(`role_id`) REFERENCES `role`(`role_id`);
ALTER TABLE
    `session` ADD CONSTRAINT `session_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `message` ADD CONSTRAINT `message_session_id_foreign` FOREIGN KEY(`session_id`) REFERENCES `session`(`session_id`);

ALTER TABLE
    `subject_combination` ADD CONSTRAINT `subject_combination_id_combination_foreign` FOREIGN KEY(`id_combination`) REFERENCES `data_score_vs_subject_combination`(`id_combination`);

ALTER TABLE
    `subject_combination` ADD CONSTRAINT `subject_combination_id_combination_foreign` FOREIGN KEY(`id_combination`) REFERENCES `subject_combination_vs_admission_subject`(`id_combination`);

ALTER TABLE
    `subject_combination_vs_admission_subject` ADD CONSTRAINT `subject_combination_vs_admission_subject_id_subject_foreign` FOREIGN KEY(`id_subject`) REFERENCES `admission_subject`(`id_subject`);

ALTER TABLE
    `bug_comment` ADD CONSTRAINT `bug_comment_bug_question_id_foreign` FOREIGN KEY(`bug_question_id`) REFERENCES `bug_question`(`id`);

ALTER TABLE
    `bug_comment` ADD CONSTRAINT `bug_comment_user_id_last_comment_foreign` FOREIGN KEY(`user_id_last_comment`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `bug_comment` ADD CONSTRAINT `bug_comment_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);

ALTER TABLE
    `bug_question` ADD CONSTRAINT `bug_question_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);