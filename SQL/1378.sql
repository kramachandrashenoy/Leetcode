https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50

Solution:

# Write your MySQL query statement below
select EUI.unique_id as unique_id,name from Employees LEFT Join EmployeeUNI as EUI
on Employees.id=EUI.id;
