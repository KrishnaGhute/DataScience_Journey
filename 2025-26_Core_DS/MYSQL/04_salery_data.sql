CREATE DATABASE IF NOT EXISTS startersql;
USE startersql;

-- Drop table if it exists to start fresh
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender ENUM('Male', 'Female', 'Other'),
    date_of_birth DATE,
    salary DECIMAL(10, 2) NOT NULL, -- Changed from INT to DECIMAL for accuracy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert 10 entries with decimal salaries
INSERT INTO users (name, email, gender, date_of_birth, salary) VALUES
('Alice', 'alice@example.com', 'Female', '1992-03-12', 55000.00),
('Bob', 'bob@example.com', 'Male', '1985-07-25', 62500.50),
('Diana', 'diana@example.com', 'Female', '1994-11-02', 48000.00),
('Ethan', 'ethan@example.com', 'Male', '1991-01-30', 71200.75),
('Fiona', 'fiona@example.com', 'Other', '1989-09-14', 53000.00),
('George', 'george@example.com', 'Male', '1993-06-08', 45000.25),
('Hannah', 'hannah@example.com', 'Female', '1987-12-22', 67000.00),
('Ian', 'ian@example.com', 'Male', '1995-04-19', 51000.00),
('Julia', 'julia@example.com', 'Female', '1990-08-05', 59300.80),
('Kevin', 'kevin@example.com', 'Male', '1986-10-11', 64000.00);

-- View the final data
SELECT * FROM users;
