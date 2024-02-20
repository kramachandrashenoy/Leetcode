Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.

For Input:
4 1 1 1 2 3 5
5
your output is: 4 

Solution:

def func(arr,k):
  l={}
  i=j=0
  summ=0
  maxi=0
  n=len(arr)
  while j<n:
    summ+=arr[j]
    if summ==k:
      if summ-k in l:
        maxi=max(j-i+1,l[summ])
      else:
        maxi=j-1+1
        l[summ]=j-i+1
    if summ>k:
      while summ>k:
        summ-=arr[i]
        i+=1
        if summ in l:
            l[summ]=max(j-i+1,l[summ])
        else:
          l[summ]=1
    j+=1
  return maxi


If negative numbers are included then we consider the following code( We use prefix sum concept)

def func(arr, k):
    l = {}
    i = j = 0
    summ = 0
    maxi = 0
    n = len(arr)
    while j < n:
        summ += arr[j]
        if summ == k:
            maxi = max(maxi, j - i + 1)
        if summ - k in l:
            maxi = max(maxi, j - l[summ - k])
        if summ not in l:
            l[summ] = j
        j += 1
    return maxi

print("The answer is " + str(func([4, 1, 1, 2, 1, 5], 5)))

      
  
