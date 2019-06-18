# Prime numbers

def isprimenumber(n):
    flag = 1
    if n==2:
        return True
    for i in range(2, n//2+1):
        if n%i==0:
            flag = 0
            return False
    if flag ==1:
        return True

# Prime Factors

def isprimefactors(n):
    if isprimenumber(n):
        return 1
    count=0
    for i in range(2, n//2+1):
        if isprimenumber(i) and n%i == 0:
            count+=1
    return count


