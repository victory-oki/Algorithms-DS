# Uses python3
def gcd(a,b):
    if(b==0):
        return(a)
    return gcd(b,a%b)
def lcm(a,b):
    if( a==0 or b==0):
        return 0
    cd = gcd(a,b)
    if (gcd == 1):
        return a*b
    elif (cd == a or cd == b):
        return max(a,b)
    else:
        return(int((min(a,b)/cd) * max(a,b)))
a, b = map(int, input().split())
print(lcm(a,b))