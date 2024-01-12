wt=[10, 20, 30]
val=[60, 100, 120]
W=50
n=3
def func(wt,val,W,n):
    if (n==0 or W==0):
        return 0
    if(wt[n-1]<=W):
        return max((val[n-1]+func(wt,val,W-wt[n-1],n-1)),func(wt,val,W,n-1))
    elif (wt[n-1]>W):
        return func(wt,val,W,n-1)
print("The maximum profit is: "+ str(func(wt,val,W,n)))
