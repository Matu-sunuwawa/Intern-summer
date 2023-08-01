
"""
1.
number = int(raw_input("Enter an integer: "))
if number < 100:
    print ("Your number is smaller than 100")
else:
    print ("Your number is greater than 100")
"""

"""
2.
n = 10
sum = 0
count = 0
while count < n:
    num = float(input(""))
    sum = sum+num
    count = count+1
average = float(sum)/n
print ("n = %d, sum = %f" % (n,sum))
print ("Average = %f" % average)
"""

"""
3.
f = 0.0
print ("far celsius")
while f <= 250:
    celsius = (f - 32.0)/1.8
    print("%6.1f %9.2f" % (f , celsius))
    f = f + 25
"""

"""
4.
a,b = 45,54
print(a,'\n',b)
a,b = b,a
print(a,"\n",b)
"""

"""
5.
data = ("Kushal", "India", "python")
name,country,lan = data
print("",name,"\n",country,"\n",lan)

data2 = ("Kushal", "India", "python")
print(data2[1])
coun = data2[1]
print(coun)
"""

"""
6.
y = "3.87"
yc = float(y)
print(type(y))
print(type(yc))
"""

"""
7.
i = 1
print("-"*50)
while i<11:
    n = 1
    while n<=10:
        print ("%4d" % (i*n), end = '')
        n+=1
    print ("")
    i +=1
print("-"*50)
"""

"""
8.
print("*"*4)
i = int(input("Enter a number: "))
while i>0:
    print("*"*i)
    i -= 1

i = int(input("Enter a number: "))
for i in range(1,i+1,1):
    print("*"*i)

i = int(input("Enter a number: "))
j = 1
while j<=i:
    print("*"*j)
    j+=1

i = int(input("Enter a number: "))
j = 1
for i in range (i,0,-1): # range(start,stop,step)
    print("*"*i)
    print(" "*j, end = '')
    j+=1
"""

"""
9.
a  = [1,342,2233423,'india','fedora']
print(a[4])
print(a[-2])
print(a[0:-1])
print(a[2:-2])
print(a[:-2])
print(a[0::3]) #start from '0' and stop at 'end' and step by '3'
print(a[0:3:2]) #start from '0' and stop at '3' and step by '2'
"""

"""
10.
a  = [1,342,2233423,'india','fedora']
b = []
if a: #list is not empty
    pass
else: #list is empty
    print("Yes empty")
if b:
    pass
else:
    print("Yes empty!")
"""

"""
#Dict - List - LIFO - FIFO
a = [1,2,3,4,5,6]
# a.pop() #LIFO
print(a.pop())  #LIFO
print(a)
a.append(34)
print(a)
# a.pop(0)    #FIFO
print(a.pop(0)) #FIFO
print(a)
print([x+1 for x in a]) #for x in a do operation 'x+1'
z = [x+1 for x in [x**2 for x in a]]    #first do 'x**2' then 'x+1'
print(z)
y = [x+3 for x in [x*2 for x in z]]
print(y)

data = {'Kushal':'Fedora','Jace':'Mac','Kart_':'Debian','parthan':'ubintu'} #dictionary
for x, y in data.items():   #accessing all in the dictionary
    print('%s uses %s' % (x,y))

data = {}   #creating/declaring the null dictionary
data.setdefault('names',[]).append('Ruby')
data.setdefault('names',[]).append('python')
data.setdefault('names',[]).append('c')
print(data)
print(data.keys())
print(data.values())
print(data['names'][2]) #accessing the dict
print(data['names'][0]) #accessing the dict
data.setdefault('type',[]).append('animal')
data.setdefault('type',[]).append('programming')
data.setdefault('type',[]).append('programming')
print(data)
data['other']='nothing'
print(data)
"""


#student.py
n = int(input("Enter the number of student: "))
data = {}
lang = ('physics','maths','history')    #set
for i in range(0, n):   #from 0 to n-1
    name = input("Enter the name of student %d: " % (i+1))
    marks = []
    for x in lang:
        marks.append(int(input("Enter the marks of %s: " % x))) #marks.append('biology')
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("%s's total marks %d" % (x, total))
    if total<120:
        print("%s failed :(" % x)
    else:
        print("%s passed :)" % x)


"""
#matrxmul.py
n = int(input("Enter the values of n:"))
print("Enter the values for matrix A")
a = []
for i in range(0,n):
    a.append([int(x) for x in input("").split(" ")])
print("Enter values for the Matrix B")
b = []
for i in range(0, n):
    b.append([int(x) for x in input("").split(" ")])
c = []
for i in range(0, n):
    c.append([a[i][j] * b[j][i] for j in range(0,n)])
print("After matrix multiplication")
print("-"*10*n)
for x in c:
    for y in x:
        print("%5d" % y, end = '')
    print("")
print("-" * 10 * n)
"""