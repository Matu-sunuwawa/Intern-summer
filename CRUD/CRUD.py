
class Signup:
    def __init__(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.value = 0
    def register(self):
        print("-------------------Registration Page-------------------")

        f1 = open(f"{self.username}Saving","x")
        f2 = open(f"{self.username}Credit","x")

        u = ' '.join(format(ord(x), 'b') for x in self.username)
        p =' '.join(format(ord(x), 'b') for x in self.password)


        with open(f"{self.username}Saving","a") as file:
            file.write(f'{u},{p},{self.value}\n')
        with open(f"{self.username}Credit","a") as file:
            file.write(f"{u},{p},{self.value}\n")
        
        print("Registration Successful!")
        print("")
        x = Signin()
        x.login()

class Signin:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
    def login(self):
        print("-------------------Login Page-------------------")
        try:
            with open(f"{self.username}Saving","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    u = ''.join(chr(int(stored_username[i*8:i*8+8],2)) for i in range(len(stored_username)//7))
                    p = ''.join(chr(int(stored_password[i*8:i*8+8],2)) for i in range(len(stored_password)//7))
                    if self.username == u and self.password == p:
                        Signin.select(self)
                        return
            print("")
            self.all()
        except:
            print("There is no such file or you may miss the wright username or password information!\nPlease be register!")
            All.all(self)
        
 