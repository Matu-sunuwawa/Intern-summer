"""
#Average of the number
n = int(input("Enter the range: "))
sum=0
for i in range(0,n):
    num = float(input("Enter the numbers: "))
    sum+=num
avg = (sum/n)
print("The Average of the numers are: %4.3f" % (avg))
"""

"""
#Temprature conversion
def ftoc():
    c = float(input("Enter the number: "))
    f = ((9/5)*c)+32
    print("The Fahrenheit is: %5.3f F" % (f))
def ctof():
    f = float(input("Enter the number: "))
    c = (f-32)*(5/9)
    print("The Celsius is: %5.3f C" % (c))

def fun():
    print("choose you want to operate?\n1.F to C\n2.C to F")
    number = int(input("choose: "))
    match number:
        case 1:
            ftoc()
        case 2:
            ctof()
        case _:
            print("Please choose the correct!!")
            fun()
fun()
"""

"""
#Fibonacci Series
num1=0
num2=1
sum=0
n = int(input("Enter the range: "))
print(f"{num1}\n{num2}")
for i in range(n):
    sum=(num1+num2)
    print(sum)
    num1=num2
    num2=sum
"""

"""
#Multiplication Table
print("-"*100)
print('\t',end='')
for i in range(10):
    print(i,end='\t')
print("")
for j in range(1,10):
    print('\t',end='')
    print(f"{j}",end='\t')
    for k in range(1,10):
        mul = j*k
        print(mul,end='\t')
    print("")
print("-"*100)
"""

"""
#Printing the '*'
n = int(input("Enter the range: "))
#style one(1)
for i in range(1,n+1,1):
    print("*"*i)
#style two(2)
for i in range(1,n+1):
    print(" "*(n-1),end='')
    print("*"*i)
    n-=1
n = int(input("Enter the range: "))
#style three(3)
for i in range(n,0,-1):
    print("*"*i)
#style four(4)
for i in range(n):
    print(" "*i,end='')
    print("*"*n)
    n-=1
"""

"""
#Students
d = {}
n = int(input("Enter the number of students: "))
language = ('physics','maths','history')
for i in range(n):
    name = str(input("Enter the name of student %d: "% (i+1)))
    mark = [] #Declaration location matters
    for i in language:
        mark.append(float(input("Enter the marks for %s: "% (i))))
    d[name] = mark
print(d)
for x,y in d.items():
    s = sum(y)
    if s < 120:
        print("Student result %3.2f and %s failed!"% (s,x))
    else:
        print("Student result %3.2f and %s passed!"% (s,x))

"""

"""
#Matrixmul
a = []
b = []
c = []
n = int(input("Enter number of matrix: "))
print("Enter the numbers 1st matrix:-")
for i in range(n):
    a.append(input("").split(" "))
print("Enter the numbers 2nd matrix:-")
for i in range(n):
    b.append(input("").split(" "))
print(a)
print(b)
for i in range(n):
    c.append([int(a[i][j])*int(b[j][i]) for j in range(n)])
print(c)
for i in range(n):
    for j in range(n):
        print(c[i][j],end = ' ')
    print("")
"""


