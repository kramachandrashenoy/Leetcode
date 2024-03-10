https://www.geeksforgeeks.org/problems/shop-in-candy-store1145/1
In a candy store, there are N different types of candies available and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
For every candy you buy from the store and get K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to find what is the minimum amount of money you have to spend to buy all the N different candies. 
Secondly, you have to find what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.

Example 1:

Input:
N = 4
K = 2
candies[] = {3 2 1 4}

Output:
3 7

Solution:
def candyStore(self, candies,N,K):
    # code here
    candies.sort()
    i=0
    j=N-1
    first=0
    while i<=j:
        first+=candies[i]
        j-=K
        i+=1
    i=N-1
    j=0
    second=0
    while j<=i:
        second+=candies[i]
        j+=K
        i-=1
    return [first,second]
                                                                                           
