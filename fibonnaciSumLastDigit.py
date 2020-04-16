# Uses python3  
def fibLastDigitSum(n):
    fibArr = [0,1]
    sumArr = [0,1]
    curSumval = 1
    pisano_period = n
    for i in range(n+1):
        if (i==0 or i ==1):
            pass
        else:
            val = (fibArr[i-1]+fibArr[i-2])%10
            curSumval += val
            sumArr.append(curSumval)
            fibArr.append(val)
            if fibArr[-2:] == [0,1]:
                pisano_period = len(fibArr) - 2
                break
    rem = n%60
    if(pisano_period == n):
        return(sumArr[n]%10)
    else:
        return(sumArr[rem]%10)
    
a = int(input())
print(fibLastDigitSum(a))