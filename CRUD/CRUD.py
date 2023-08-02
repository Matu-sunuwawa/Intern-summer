
class Signup:
    def __init__(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
    def register(self):
        print("-------------------Registration Page-------------------")

        f1 = open(f"{self.username}","x")


        with open(f"{self.username}","a") as file:
            file.write(f'{self.username},{self.password}\n')
        
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
            with open(f"{self.username}","r") as file:
                for line in file:
                    stored_username,stored_password = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        print("It is Ok!")
                        return
            print("")
        except:
            print("There is no such file or you may miss the wright username or password information!\nPlease be register!")
            All.all(self)
        
class All:
    def all(self):
        print("1.signin\n2.signup\n3.exit")
        number = int(input("Enter a number: "))

        match number:
            case 1:
                x = Signin()
                x.login()
            case 2:
                x = Signup()
                x.register()
            case 3:
                exit
            case _:
                print("Please follow the above guide")
                all()

x = All()
x.all()