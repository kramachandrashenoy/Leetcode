https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50

Solution:

# Write your MySQL query statement below
select product_name,year,price from Product,Sales 
where Sales.product_id=Product.product_id;
