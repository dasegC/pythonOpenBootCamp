PI = 3.14152119

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def como_me_llamo():
    return __name__

class Operador:
    def Multiplicacion(self,a,b):
        return a*b


def weird(n):
    if n % 2 == 1 or (n % 2 == 0 and n >= 6 and n <= 20):
        print('Weird')
    else:
        print('Not Weird')
    
        
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiply(a,b):
    return a*b
""" 
def set_function(a,b):
    x = list(a.difference(b))
    y = list(b.difference(a))
    list = sorted(x+y)
    for i in list:
        print(i)

if __name__ == '__main__':
    m = int(input())
    a = set(map(int,input().split()))
    n = int(input())
    b = set(map(int,input().split()))
    result = set_function(a,b)

 """

""" 
def set_function(a, b):
    k = a.difference(b)
    j = b.difference(a)
    u = list(k)
    v = list(j)
    l = u + v
    m = sorted(l)
    
    for i in m:
        print(i)

if __name__ == '__main__':
    x = int(input())
    x = set(map(int, input().split()))
    y = int(input())
    y = set(map(int, input().split()))
    result = set_function(x, y)
"""





""" # Enter your code here. Read input from STDIN. Print output to STDOUT
def happiness():
    n,m = input().split()
    ar=list(map(int,input().split()))
    a=set(map(int,input().split()))
    b=set(map(int,input().split()))
    happy=0
    for i in ar:
        if i in a:
            happy += 1
        if i in b:
            happy -=1
    print(happy)
    
    if __name__ == '__main__':
        happiness()
         """



""" def subcampeon(arr, conjunto):
    for i in arr:
        conjunto.add(i)
    conjunto.remove(max(conjunto))
    print(max(conjunto))
    

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    conjunto = set()
    subcampeon(arr, conjunto) """
    
    

""" 
if __name__ == '__main__':
n = int(input())
arr = map(int, input().split())
s=set()
for i in arr:
    s.add(i)
s.remove(max(s))
print(max(s))

 """
""" if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) """