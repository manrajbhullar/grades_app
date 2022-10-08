CREATE DATABASE grades_app;

USE grades_app;

CREATE TABLE grades (
    id int NOT NULL AUTO_INCREMENT,
    course varchar(25) NOT NULL,
    first_name varchar(25) NOT NULL,
    last_name  varchar(25) NOT NULL,
    grade float NOT NULL,
    PRIMARY KEY (id)
);
