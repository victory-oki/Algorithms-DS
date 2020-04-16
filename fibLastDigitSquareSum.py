# Uses python3
def fibLastDigitSquareSum(n):
    fibArr = [0,1]
    sqArr = [] 
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
    for i in fibArr:
        sqArr.append(i*i)
    return(sum(sqArr[0:rem+1])%10)
a = int(input())
print(fibLastDigitSquareSum(a))