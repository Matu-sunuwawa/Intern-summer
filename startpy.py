# print("Hello World")
# print("Let's Begin")
# print("Wow")

def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open("users.txt","a") as file:
        file.write(f"{username},{password}\n")
    
    print("Registration Successful!")
# register()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("users.txt","r") as file:
        for line in file:
            stored_username,stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login Successful!")
                return
    print("Invalid username or password. Please try again.")

# login()

def modify(file_path,line_num,new_line):
    # num = input("Enter a number: ")
    with open("users.txt",'r') as file:
        lines = file.readlines()
    
    if line_num <= len(lines):
        lines[line_num-1] = new_line + '\n'

        with open("users.txt",'w') as file:
            #wriet all modified lines
            lines[0] = "matyas,mama,100\n"
            lines[1] = "mahlet,mama,0"
            file.writelines(lines)
    else:
        print(f"Invalid line the file contains {len(lines)} line(s)")
file_path = 'users.txt'
line_num = 2
new_line = 'This is the new line txt'
# modify(file_path,line_num,new_line)

"""
def b(bb):
    b1 =bb
    deci, i, n = 0, 0, 0
    while(bb !=0):
        dec = bb % 10
        deci = deci + dec * pow(2, i)
        bb = bb//10
        i += 1
    return (deci)

bin = '1000111 1100101 1100101 1101011 1110011'
print("binary value: " , bin)
str_data = ''

for i in range(0, len(bin), 7):
    temp = int(bin[i:i + 7])
    decimal = b(temp)
    str_data = str_data + chr(decimal)

print("the value: ",str_data)
"""

str = "hello"
m = ' '.join(format(ord(x), 'b') for x in str)
# print(m)

x = "1101000 1100101 1101100 1101100 1101111"
# print(chr(int(x[:8], 2)))

def de(x):
    return ''.join(chr(int(x[i*8:i*8+8],2)) for i in range(len(x)//8))

de(x)

# ma = ' '.join(chr(int(bits[i*8:i*8+8],2)) for i in range(len(bits)//8))

#------------worked
x = "1101000 1100101 1101100 1101100 1101111"
bits = "0110100001101001"
# bits = "1101000 1101001"
# ma = ' '.join(chr(int(bits[i*8:i*8+8],2)) for i in range(len(bits)//8))
# print(ma)

ma = ''.join(chr(int(x[i*8:i*8+8],2)) for i in range(len(x)//7))
print(ma)

# print(chr(int(bits[8:], 2)))
n = int(bits, 2)
n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()