# Uses python3
def fibLastDigitPartialSum(n,m):
    fibArr = [0,1]
    sumArr = [0,1]
    pisano_period = n
    for i in range(n+1):
        if (i==0 or i ==1):
            pass
        else:
            val = (fibArr[i-1]+fibArr[i-2])%10
            fibArr.append(val)
            if fibArr[-2:] == [0,1]:
                pisano_period = len(fibArr) - 2
                break
    rem = n%60
    if(pisano_period == n):
        return(sum(fibArr[m%60:n+1])%10)
    else:
        return(sum(fibArr[m%60:rem+1])%10)
    
a,b = map(int,input().split())
print(fibLastDigitPartialSum(b,a))