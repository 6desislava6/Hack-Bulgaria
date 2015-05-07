SELECT Firstname, LastName, Title FROM employees;
SELECT * FROM employees WHERE city = 'Seattle';
SELECT * FROM employees WHERE city = 'LONdON';
SELECT * FROM employees WHERE Title LIKE '%Sales%';
SELECT * FROM ewhmployees WHERE Title LIKE '%Sales%' AND (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.') ;
SELECT * FROM employees ORDER BY BirthDate LIMIT 5;
SELECT * FROM employees ORDER BY HireDate LIMIT 5;
SELECT * FROM employees WHERE ReportsTo is null;
SELECT a.FirstName, b.FirstName
FROM employees AS a JOIN employees AS b ON a.ReportsTo = b.EmployeeID;
SELECT COUNT(*) FROM employees
WHERE (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.') ;
SELECT COUNT(*) FROM employees
 WHERE (TitleOfCourtesy = 'Mr.' OR TitleOfCourtesy = 'Dr.') ;
SELECT * FROM (SELECT DISTINCT City FROM employees)
AS a JOIN (SELECT FirstName, City FROM employees) AS b ON a.City = b.City;
SELECT * FROM (SELECT DISTINCT City FROM employees)
AS a JOIN (SELECT FirstName, City FROM employees) AS b ON a.City = b.City;
SELECT count(*) FROM employees GROUP BY City;
SELECT ORDERID, FirstName, LastName FROM orders JOIN
employees ON orders.EmployeeID = employees.EmployeeID;
SELECT ORDERID, CompanyName FROM orders JOIN shippers ON orders.ShipVia = shippers.ShipperID;
SELECT count(*) FROM orders GROUP BY ShipCountry;
SELECT count(*), EmployeeID FROM orders
 GROUP BY EmployeeID;
SELECT FirstName, LastName FROM employees AS a inner JOIN
 orders AS b ON a.EmployeeID = b.EmployeeID
GROUP BY b.EmployeeID
ORDER BY count(b.EmployeeID) DESC LIMIT 1;
SELECT CompanyName FROM customers AS a inner JOIN orders
 AS b ON a.CustomerID = b.CustomerID
GROUP BY b.CustomerID
ORDER BY count(b.CustomerID) DESC LIMIT 1;
SELECT ORDERID, FirstName, CompanyName FROM
((orders JOIN employees ON orders.EmployeeID = employees.EmployeeID)
 AS a JOIN customers ON a.CustomerID = customers.CustomerID);
SELECT a.ORDERID, b.CompanyName, c.CompanyName
FROM orders AS a
JOIN customers AS b
ON a.CustomerID = b.CustomerID
JOIN shippers AS c
ON a.ShipVia = c.ShipperID;
