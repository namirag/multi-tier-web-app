CREATE DATABASE IF NOT EXISTS shop;
USE shop;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES ('Test User', 'test@mail.com');
