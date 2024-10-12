CREATE DATABASE IF NOT EXISTS membership_db;
USE membership_db;

-- Create transport_types 
CREATE TABLE transport_types (
    type VARCHAR(10) PRIMARY KEY
);

-- Insert transport 
INSERT INTO transport_types (type) VALUES 
    ('bus'),
    ('travel');

-- Create members 
CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    transport_type VARCHAR(10) NOT NULL,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (transport_type) REFERENCES transport_types(type)
);

-- Create attendances 
CREATE TABLE attendances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    check_in_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    attendance_number INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(id)
);

-- Create payments 
CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    attendance_cycle INT NOT NULL,
    FOREIGN KEY (member_id) REFERENCES members(id)
);


CREATE INDEX idx_member_code ON members(code);
CREATE INDEX idx_attendance_member ON attendances(member_id);
CREATE INDEX idx_payment_member ON payments(member_id);
CREATE INDEX idx_attendance_check_in ON attendances(check_in_time);
CREATE INDEX idx_payment_date ON payments(payment_date);
