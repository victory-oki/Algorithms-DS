# Uses python3
def fibLastDigit(n,m):
    fibArr = [0,1]
    pisano_period = n
    for i in range(n+1):
        if (i==0 or i ==1):
            pass
        else:
            val = (fibArr[i-1]+fibArr[i-2])%m
            fibArr.append(val)
            if fibArr[-2:] == [0,1]:
                pisano_period = len(fibArr) - 2
                break
    rem = n% pisano_period
    if(pisano_period == n):
        return(fibArr[n])
    else:
        return(fibArr[rem])
a, b = map(int, input().split())
print(fibLastDigit(a,b))