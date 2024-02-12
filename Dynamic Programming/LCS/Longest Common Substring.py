# If there is a discontinuity we make the cell 0 and to calculate the longest substring we go through the matrix and store the maximum value
def func(a,b,m,n):
  t=[[0 for i in range(n+1)] for j in range(m+1)]
  maxi=0

  for i in range(m+1):
    for j in range(n+1):
      if i==0 or j ==0:
        t[i][j]=0
      else:
        if a[m-1] == b[n-1]:
          t[i][j]=1+t[i-1][j-1]
          maxi=max(maxi ,t[i][j])
        else:
          t[i][j]=0
    # Printing the LCS
  i=m
  j=n
  ans=str()
  while(i>0 and j>0):
    if a[i-1]==b[j-1]:
      ans+=a[i-1]
      i-=1
      j-=1
    else:
      if t[i-1][j]>t[i][j-1]:
        i-=1
      else:
        j-=1
    print("The Longest common subsequence is "+ans[::-1])
