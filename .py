-- ============================================
-- E-COMMERCE DATABASE - COMPLETE DDL SCRIPT
-- ============================================

-- 1. Create Database
CREATE DATABASE ECommerceDB;

-- 2. Select Database
USE ECommerceDB;


-- ============================================
-- 3. Create Products Table
-- ============================================

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    ProductCategory VARCHAR(50) NOT NULL,
    ProductPrice DECIMAL(10,2) NOT NULL,
    ProductStock INT DEFAULT 0
);


-- ============================================
-- 4. Create Customers Table
-- ============================================

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerName VARCHAR(100) NOT NULL,
    CustomerEmail VARCHAR(100) UNIQUE NOT NULL,
    CustomerPhone VARCHAR(15)
);


-- ============================================
-- 5. Create Orders Table
-- ============================================

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ProductID INT NOT NULL,
    OrderDate DATE NOT NULL,
    Quantity INT NOT NULL,
    TotalAmount DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (CustomerID)
        REFERENCES Customers(CustomerID),

    FOREIGN KEY (ProductID)
        REFERENCES Products(ProductID)
);


-- ============================================
-- 6. Add Indexes to Products Table
-- ============================================

CREATE INDEX idx_ProductName
ON Products(ProductName);

CREATE INDEX idx_ProductCategory
ON Products(ProductCategory);


-- ============================================
-- 7. Create CustomerOrders View
-- ============================================

CREATE VIEW CustomerOrders AS
SELECT
    c.CustomerID,
    c.CustomerName,
    c.CustomerEmail,
    c.CustomerPhone,
    o.OrderID,
    o.OrderDate,
    o.ProductID,
    o.Quantity,
    o.TotalAmount
FROM Customers c
JOIN Orders o
    ON c.CustomerID = o.CustomerID;


-- ============================================
-- 8. Query the CustomerOrders View
-- ============================================

SELECT *
FROM CustomerOrders;


-- ============================================
-- 9. Drop Products Table
-- ============================================

DROP TABLE Products;


-- ============================================
-- 10. Recreate Products Table
--     with ProductDescription
-- ============================================

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(100) NOT NULL,
    ProductCategory VARCHAR(50) NOT NULL,
    ProductDescription VARCHAR(255),
    ProductPrice DECIMAL(10,2) NOT NULL,
    ProductStock INT DEFAULT 0
);


-- ============================================
-- 11. Recreate Indexes
-- ============================================

CREATE INDEX idx_ProductName
ON Products(ProductName);

CREATE INDEX idx_ProductCategory
ON Products(ProductCategory);


-- ============================================
-- 12. Modify Customers Table
--     Add CustomerAddress
-- ============================================

ALTER TABLE Customers
ADD CustomerAddress VARCHAR(255);


-- ============================================
-- 13. Display Table Structures
-- ============================================

DESCRIBE Products;

DESCRIBE Customers;

DESCRIBE Orders;


-- ============================================
-- 14. Display Database Tables
-- ============================================

SHOW TABLES;


-- ============================================
-- 15. Display CustomerOrders View
-- ============================================

SELECT *
FROM CustomerOrders;
