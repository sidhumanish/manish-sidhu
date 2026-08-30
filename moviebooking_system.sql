CREATE DATABASE IF NOT EXISTS moviebooking;
USE moviebooking;
-- Create the Movies table
CREATE TABLE IF NOT exists Movies (
    movie_name VARCHAR(255)	,
    genre VARCHAR(50),
    duration INT,           -- Duration in minutes
    language VARCHAR(50),
    rating FLOAT
);

-- Create the Showtimes table
CREATE TABLE IF NOT exists Showtimes (
    movie_name varchar(255)	REFERENCES Movies(movie_name),
    show_date DATE,
    show_time TIME,
    available_seats INT,
    price FLOAT
);

-- Create the Users table
CREATE TABLE IF NOT exists Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(255),
    email VARCHAR(100),
    phone VARCHAR(15)
);

-- Create the Bookings table
CREATE TABLE IF NOT exists Bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT	REFERENCES Users(user_id),
    password VARCHAR(200) REFERENCES Users(password),
    seats_booked INT,
    total_amount FLOAT,
    booking_date DATE);

-- Create the Admin table 
CREATE TABLE IF NOT exists Admin (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    adminpassword VARCHAR(255)
);
INSERT INTO Admin(admin_id,name,adminpassword)
	VALUES(1,'MB','VN');
INSERT INTO Admin(admin_id,name,adminpassword)
	VALUES(2,'Manish','Sidhu');
INSERT INTO Admin(admin_id,name,adminpassword)
	VALUES(3,'Bhavesh','Nyol');
