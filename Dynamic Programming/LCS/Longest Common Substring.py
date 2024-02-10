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
