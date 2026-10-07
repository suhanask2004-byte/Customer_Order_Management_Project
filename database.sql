CREATE DATABASE IF NOT EXISTS Sales_customers_database_management;

USE Sales_customers_database_management;

CREATE TABLE IF NOT EXISTS salespeople (
    snum INT PRIMARY KEY,
    sname VARCHAR(50),
    city VARCHAR(50),
    comm DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS customer (
    cnum INT PRIMARY KEY,
    cname VARCHAR(50),
    city VARCHAR(50),
    snum INT,
    FOREIGN KEY (snum) REFERENCES salespeople(snum)
);

CREATE TABLE IF NOT EXISTS orders (
    onum INT PRIMARY KEY,
    odate DATE,
    oamount DECIMAL(10,2),
    cnum INT,
    snum INT,
    FOREIGN KEY (cnum) REFERENCES customer(cnum),
    FOREIGN KEY (snum) REFERENCES salespeople(snum)
);
