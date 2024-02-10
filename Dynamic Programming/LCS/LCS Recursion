# Given two strings a and b of length m and n find the longest common subsequence.

def func(a,b,m,n):
  if n==0 or m==0:
    return 0
  if(a[m-1] == b[n-1]):
    return 1+func(a,b,m-1,n-1)
  else:
    return max(func(a,b,m,n-1),func(a,b,m-1,n))

print("The length  of the longest commom subsequence is "+str(func(a,b,m,n)))
