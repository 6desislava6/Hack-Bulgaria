Select Firstname, LastName, Title FROM employees;
Select * FROM employees where city = 'Seattle';
Select * FROM employees where city = 'London';
Select * FROM employees where Title LIKE '%Sales%';
Select * FROM employees where Title LIKE '%Sales%' AND (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.') ;
Select * FROM employees ORDER BY BirthDate LIMIT 5;
Select * FROM employees ORDER BY HireDate LIMIT 5;
Select * FROM employees where ReportsTo is null;
Select a.FirstName, b.FirstName from employees as a JOIN employees as b on a.ReportsTo = b.EmployeeID;
Select COUNT(*) FROM employees WHERE (TitleOfCourtesy = 'Ms.' OR TitleOfCourtesy = 'Mrs.') ;
Select COUNT(*) FROM employees WHERE (TitleOfCourtesy = 'Mr.' OR TitleOfCourtesy = 'Dr.') ;
SELECT * FROM (SELECT DISTINCT City From employees) as a JOIN (select FirstName, City from employees) as b ON a.City = b.City;
SELECT * FROM (SELECT DISTINCT City From employees) as a JOIN (select FirstName, City from employees) as b ON a.City = b.City;
Select count(*) from employees group by City;
Select OrderID, FirstName, LastName From orders JOIN employees ON orders.EmployeeID = employees.EmployeeID; 
Select OrderID, CompanyName From orders JOIN shippers ON orders.ShipVia = shippers.ShipperID; 
Select count(*) from orders group by ShipCountry;
Select count(*), EmployeeID from orders group by EmployeeID;
Select FirstName, LastName from employees as a inner join orders as b on a.EmployeeID = b.EmployeeID 
group by b.EmployeeID
order by count(b.EmployeeID) desc limit 1; 
Select CompanyName from customers as a inner join orders as b on a.CustomerID = b.CustomerID 
group by b.CustomerID
order by count(b.CustomerID) desc limit 1; 
Select OrderID, FirstName, CompanyName FROM ((orders JOIN employees ON orders.EmployeeID = employees.EmployeeID) as a JOIN customers ON a.CustomerID = customers.CustomerID);
SELECT a.OrderID, b.CompanyName, c.CompanyName
FROM orders AS a
JOIN customers as b
on a.CustomerID = b.CustomerID
JOIN shippers as c
ON a.ShipVia = c.ShipperID;