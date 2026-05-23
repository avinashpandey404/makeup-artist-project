CREATE DATABASE IF NOT EXISTS makeupdb;

USE makeupdb;

CREATE TABLE bookings (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    booking_date DATE,
    service VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE contacts (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(255),
    email VARCHAR(255),
    message TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
