class solution:
  def func():
    if m==0 or n==0:
      return 0
    if t[m][n] != -1:
      return t[m][n]
    if (a[m-1] == b[n-1]:
      return t[m][n]=1+func(a,b,m-1,n-1)
    else:
      return t[m][n]=max(func(a,b,m,n-1),func(a,b,m-1,n))
      
    

  def mainfunc(a,b,m,n):
    t=[[-1 for i in range(n+1)]for j in range(m+1)]
    print("The length of the longest commom subsequence is "+str(func(a,b,m,n)))
