#recursion:calls itself

def fact(n):
    if n==0 or n==1:
        return 1
    #as only the positive int have the factorial value
    elif n>1:
        return n*fact(n-1)
n = int(input())
print(fact(n))