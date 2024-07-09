https://leetcode.com/problems/employee-bonus/description/?envType=study-plan-v2&envId=top-sql-50

Solution:

select name,bonus from Employee left join Bonus 
on Employee.empId=Bonus.empId
where bonus<1000 or bonus is NUll;
