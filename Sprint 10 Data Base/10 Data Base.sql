-- Given a database with (at least) two tables: customers and orders as shown below, 
-- write an SQL query that returns the customer name, city and amount for all orders between $100 and $3500 inclusive, grouped by name and ordered by city.

-- result for example

-- name                  city                  totalSum
-- --------------------  --------------------  ---------------
-- Graham Zusi           California            261
-- Jozy Altidore         Kyiv                  2000.0
-- Brad Guzan            London                270.65
-- Julian Green          London                250.45
-- Nick Rimando          New York              3210.86

-- First 5 rows of "customers" table, ordered by id
-- id      name             city          grade   salesperson_id
-- ------  ---------------  ------------  ------  --------------
-- 3001    Brad Guzan       London        100     5005
-- 3002    Nick Rimando     New York      100     5001
-- 3003    Jozy Altidore    Kyiv          200     5007
-- 3004    Fabian Johns     Paris         300     5006
-- 3005    Graham Zusi      California    200     5002 
-- First 5 rows of "orders" table ordered by order_num
-- order_num   amount     date        customer_id  saleperson_id
-- ----------  ---------  ----------  -----------  -------------
-- 70001       150.5      2022-10-05  3005         5002
-- 70002       65.26      2022-10-05  3002         5001
-- 70003       2480.4     2022-10-10  3009         5003
-- 70004       110.5      2022-08-17  3005         5003
-- 70005       2400.6     2022-07-27  3007         5001
-- For example:

-- Test	Result
-- -- Testing with original db
-- name                  city                  totalSum
-- --------------------  --------------------  ---------------
-- Geoff Cameron         Berlin                2590.9
-- Graham Zusi           California            1099.0
-- Brad Guzan            London                270.65
-- Julian Green          London                250.45
-- Brad Davis            New York              2400.6
-- Nick Rimando          New York              3210.86
-- Fabian Johns          Paris                 1983.43




SELECT name, city, SUM(amount) totalSum
FROM orders INNER JOIN customers
ON customers.id = orders.customer_id 
WHERE amount>=100 and amount<=3500
GROUP BY name
ORDER BY city;




-- Given a database with (at least) a table customers as shown below, write an SQL query that insert in to table new customer 
-- with  name Stefan Huk ,id 3006, city Kyiv and grade 500, salesperson_id 5007  .
-- After insert write an SQL query that returns the all columns of all customers who live in London or Kyiv, in ascending order of id.

-- .

-- First 5 rows of customers table, ordered by id
-- id      name             city          grade   salesperson_id
-- ------  ---------------  ------------  ------  --------------
-- 3001    Brad Guzan       London        100     5005
-- 3002    Nick Rimando     New York      100     5001
-- 3003    Jozy Altidore    Kyiv          200     5007
-- 3004    Fabian Johns     Paris         300     5006
-- 3005    Graham Zusi      California    200     5002 

-- For example:

-- Test	Result
-- -- Testing with original db
-- id               name        city   grade       salesperson_id
-- ---------------  ----------  -----  ----------  --------------
-- 3001             Brad Guzan  Londo  100         5005
-- 3006             Stefan Huk  Kyiv   500         5007
-- 3008             Julian Gre  Londo  300         5002



INSERT INTO customers (id,name,city,grade,salesperson_id) VALUES (3006,'Stefan Huk', 'Kyiv', 500, 5007);
SELECT * FROM customers WHERE city IN ("London", "Kyiv") ORDER BY id;






-- Given a database with (at least) two tables: customers and orders as shown below, write an SQL query that returns the order_num, order amount and customer name for all orders between $500 and $2000 inclusive, ordered by order_num.

-- First 5 rows of customers table, ordered by id
-- id      name             city          grade   salesperson_id
-- ------  ---------------  ------------  ------  --------------
-- 3001    Brad Guzan       London        100     5005
-- 3002    Nick Rimando     New York      100     5001
-- 3003    Jozy Altidore    Kyiv          200     5007
-- 3004    Fabian Johns     Paris         300     5006
-- 3005    Graham Zusi      California    200     5002 
-- First 5 rows of orders table ordered by order_num
-- order_num   amount     date        customer_id  saleperson_id
-- ----------  ---------  ----------  -----------  -------------
-- 70001       150.5      2022-10-05  3005         5002
-- 70002       65.26      2022-10-05  3002         5001
-- 70003       2480.4     2022-10-10  3009         5003
-- 70004       110.5      2022-08-17  3009         5003
-- 70005       2400.6     2022-07-27  3007         5001
-- For example:

-- Test	Result
-- -- Testing with original db
-- order_num   amount      name
-- ----------  ----------  ---------------
-- 70007       948.5       Graham Zusi
-- 70010       1983.43     Fabian Johns
-- Answer:(penalty regime: 0 %)


SELECT order_num, amount, name
FROM orders o JOIN customers ON  o.customer_id = customers.id
WHERE o.customer_id = customers.id
AND o.amount BETWEEN 500 AND 2000
ORDER BY amount



-- Given a database with (at least) a table customers as shown below, write an SQL query that returns the name, city and grade of all customers who live in London or Paris, in ascending order of name.

-- First 5 rows of customers table, ordered by id
-- id      name             city          grade   salesperson_id
-- ------  ---------------  ------------  ------  --------------
-- 3001    Brad Guzan       London        100     5005
-- 3002    Nick Rimando     New York      100     5001
-- 3003    Jozy Altidore    Kyiv          200     5007
-- 3004    Fabian Johns     Paris         300     5006
-- 3005    Graham Zusi      California    200     5002 

-- For example:
-- Test	Result
-- -- Testing with original db
-- name             city        grade
-- ---------------  ----------  -----
-- Brad Guzan       London      100
-- Fabian Johns     Paris       300
-- Julian Green     London      300
-- Answer:(penalty regime: 0 %)


SELECT name, city, grade FROM customers
WHERE city IN ("London", "Paris")
ORDER BY name





-- Given a database with (at least) a table "customers" as shown below, write an SQL query that Update in to "customers" table , 
-- a customer  named Jozy Altidore ,id 3003, from city Kyiv to city Paris and from grade 500 to grade 300 , salesperson_id 5007  .
-- After Update write an SQL query that returns the columns name, city and grade of all customers who live in London or Paris, in ascending order of id.

-- First 5 rows of customers table, ordered by id
-- id      name             city          grade   salesperson_id
-- ------  ---------------  ------------  ------  --------------
-- 3001    Brad Guzan       London        100     5005
-- 3002    Nick Rimando     New York      100     5001
-- 3003    Jozy Altidore    Kyiv          200     5007
-- 3004    Fabian Johns     Paris         300     5006
-- 3005    Graham Zusi      California    200     5002 

-- For example:
-- Test	Result
-- -- Testing with original db
-- name                  city             grade
-- --------------------  ---------------  ----------
-- Brad Guzan            London           100
-- Jozy Altidore         Paris            300
-- Fabian Johns          Paris            300
-- Julian Green          London           300
-- Answer:(penalty regime: 0 %)


UPDATE customers 
SET city = 'Paris', grade = '300'
WHERE id = 3003;

SELECT name, city, grade FROM customers
WHERE city IN ("London", "Paris")
ORDER BY id
