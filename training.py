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

