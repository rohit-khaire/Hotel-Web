CREATE DATABASE hotel_system;

USE hotel_system;

CREATE TABLE hotels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT,
    room_number VARCHAR(20),
    image_url VARCHAR(255),
    is_booked BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (hotel_id) REFERENCES hotels(id)
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,
    username VARCHAR(255),
    checkin_date DATETIME,
    checkout_date DATETIME,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

INSERT INTO hotels (name, location) VALUES
('Hotel Sunshine', 'Mumbai'),
('Hotel GreenView', 'Pune'),
('Hotel BlueMoon', 'Delhi');