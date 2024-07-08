https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

Solution:
  
# Write your MySQL query statement below
select customer_id,COUNT(Visits.visit_id) as count_no_trans from Visits 
where Visits.visit_id not in (select DISTINCT Visits.visit_id from Visits,Transactions where Visits.visit_id=Transactions.visit_id)
GROUP BY customer_id;
