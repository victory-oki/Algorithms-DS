# Uses python3
def fibLastDigit(n):
    pisano_period = n
    fibArr = [0,1]
    for i in range(n+1):
        if (i==0 or i ==1):
            pass
        else:
            fibArr.append((fibArr[i-1]+fibArr[i-2])%10)
            if fibArr[-2:] == [0,1]:
                pisano_period = len(fibArr) - 2
                break
    rem = n%pisano_period
    if(pisano_period == n):
        return(fibArr[n])
    else:
        return(fibArr[rem])
a= int(input())
print(fibLastDigit(a))