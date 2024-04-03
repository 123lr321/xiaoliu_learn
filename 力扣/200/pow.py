#这是注释
def myPow(x, n):
        sum=1
        if n==0:
            return 1
        elif n>0:
            sum=x
            for i in range(1,n):
                sum*=x
            return sum
        else:
             for i in range(1,-n+1):
                 sum=sum/x
             return sum
print(myPow(2,10))
