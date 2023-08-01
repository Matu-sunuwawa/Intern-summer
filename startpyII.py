
import json

class Signup:
    def __init__(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        self.value = 0
    def register(self):
        print("-------------------Registration Page-------------------")
        # username = input("Enter a username: ")
        # password = input("Enter a password: ")
        # value = 0

        f1 = open(f"{self.username}Saving","x")
        f2 = open(f"{self.username}Credit","x")

        with open(f"{self.username}Saving","a") as file:
            file.write(f'{self.username},{self.password},{self.value}\n'.encode('utf-8'))
        with open(f"{self.username}Credit","a") as file:
            file.write(f"{self.username},{self.password},{self.value}\n".encode('utf-8'))
        
        print("Registration Successful!")
        print("")
        # Signin.login(self)
        x = Signin()
        x.login()

class Signin:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
    def login(self):
        print("-------------------Login Page-------------------")
        # username = input("Enter your username: ")
        # password = input("Enter your password: ")
        try:
            with open(f"{self.username}Saving","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        # print("Login Successful!")
                        Signin.select(self)
                        return
            # print("Invalid username or password. Please try again.")
            print("")
            self.all()
        except:
            print("There is no such file or you may miss the wright username or password information!\nPlease be register!")
            All.all(self)
    
    def select(self):
        print("1.Saving Account\n2.Credit Account\n3.goback")
        number = int(input("Enter a number: "))

        match number:
            case 1:
                Signin.saving(self)
            case 2:
                Signin.credit(self)
            case 3:
                All.all(self)
            case _:
                print("Please follow the above guide!")
                Signin.select(self)
        
    def saving(self):
        print("1.View\n2.Deposit\n3.Withdraw")

        number = int(input("Enter a number: "))

        match number:
            case 1:
                Signin.viewSaving(self)
            case 2:
                Signin.depositSaving(self)
            case 3:
                Signin.withdrawSaving(self)
            case _:
                print("Please follow the above guide!")
                Signin.saving(self)

    def viewSaving(self):
        """
            with open("userpy.txt","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    # print("Login Successful!")
                    select()
                    return
        """
        with open(f"{self.username}Saving","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
                if self.username == stored_username and self.password == stored_password:
                    nvalue = stored_value
                    print(f"Your Saving account is: {nvalue}")
                    # print(nvalue)
        
        Signin.otherSaving(self)
        # def other(self):
        #     print("1.Continue\n2.Cancel")

        #     number = int(input("Enter a number: "))

        #     match number:
        #         case 1:
        #             Signin.saving(self)
        #         case 2:
        #             exit
        #         case _:
        #             print("Please follow the above guide!")
        #             Signin.other(self)
        # Signin.other(self)
            # Signin.other(self)

    def otherSaving(self):
        print("1.Continue\n2.Cancel")

        number = int(input("Enter a number: "))

        match number:
            case 1:
                Signin.saving(self)
            case 2:
                exit
            case _:
                print("Please follow the above guide!")
                Signin.otherSaving(self)


    # def convert(stored_value):
    #     try:
    #         integer = int(stored_value)
    #     except ValueError:
    #         print("The String Error")
    #         return None
    #     return integer

    """
    def deposit():
        amt = int(input("Enter the amount: "))
        with open("userpy.txt","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
                # integer = convert(stored_value)

                username = stored_username
                password = stored_password
                value = int(stored_value)
                # value = stored_value
                # value = int(value)
                # namt = integer + amt

                modify_lines = [line.replace("old", "new")
                for line in lines]

        with open("userpy.txt","w") as file:
            file.write(f"{username},{password},{namt}")
    """

    def depositSaving(self):
        """
            with open("userpy.txt","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    # print("Login Successful!")
                    select()
                    return
            
            with open("userpy.txt","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        nvalue = stored_value
                        print(nvalue)
        """

        """
        amt = int(input("Enter the amount: "))
        with open("userpy.txt","r+") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
            # lines = file.readlines()
            # integer = convert(stored_value)
            integer = int(stored_value)
            nvalue = integer + amt

            modify_lines = [line.replace("stored_value", "nvalue")
            for line in file]

            file.seek(0)
        file.writelines(modify_lines)
        file.truncate()
        """
        amt = input("Enter the amount: ")
        # ---------------basic Operations------------------
        if int(amt) < 0 :
            print("Invalid Input try again!")
            Signin.depositSaving(self)
        else:
            with open(f"{self.username}Saving","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        # self.value = int(amt) + int(stored_value)
                        with open(f"{self.username}Saving","w") as file:
                            self.value = int(amt) + int(stored_value)
                            file.write(f"{self.username},{self.password},{self.value}\n")
                            file.close()
                        return
            file.close()
                    # else:
                    #     with open("userpy.txt","w") as file:
                    #         file.write(f"{stored_username},{stored_password},{stored_value}")

    def withdrawSaving(self):
        with open(f"{self.username}Saving","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
        amt = input("Enter the amount: ")
        #---------------basic Operations------------------
        if int(amt) < 0:
            print("Invalid Input")
            Signin.withdrawSaving(self)
        elif int(amt) > int(stored_value):
            print("Not enough balance!")
            Signin.withdrawSaving(self)
        else:
            with open(f"{self.username}Saving","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        nvalue = int(stored_value) - int(amt)
            # print("Invalid username or password. Please try again.")

            with open(f"{self.username}Saving","w") as file:
                file.write(f"{stored_username},{stored_password},{nvalue}\n")

    def credit(self):
        print("1.View\n2.Deposit\n3.Withdraw")

        number = int(input("Enter a number: "))

        match number:
            case 1:
                Signin.viewCredit(self)
            case 2:
                Signin.depositCredit(self)
            case 3:
                Signin.withdrawCredit(self)
            case _:
                print("Please follow the above guide!")
                Signin.saving(self)

    def viewCredit(self):
        with open(f"{self.username}Credit","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
                if self.username == stored_username and self.password == stored_password:
                    nvalue = stored_value
                    print(f"Your Credit account is: {nvalue}")
                    # print(nvalue)
        
        Signin.otherCredit(self)

    def otherCredit(self):
        print("1.Continue\n2.Cancel")

        number = int(input("Enter a number: "))

        match number:
            case 1:
                Signin.credit(self)
            case 2:
                exit
            case _:
                print("Please follow the above guide!")
                Signin.otherCredit(self)
        
    def depositCredit(self):
        with open(f"{self.username}Credit","r") as file:
            for line in file:
                stored_username,stored_password,stored_value = line.strip().split(",")
        amt = input("Enter the amount: ")
        #---------------basic Operations------------------
        if int(amt) < 0:
            print("Invalid Input")
            Signin.depositCreditCredit(self)
        elif int(amt) > int(stored_value):
            print("It is not Saving account!")
            Signin.depositCredit(self)
        else:
            with open(f"{self.username}Credit","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        nvalue = int(stored_value) - int(amt)
            # print("Invalid username or password. Please try again.")

            with open(f"{self.username}Credit","w") as file:
                file.write(f"{stored_username},{stored_password},{nvalue}\n")
        
    def withdrawCredit(self):
        amt = input("Enter the amount: ")
        # ---------------basic Operations------------------
        if int(amt) < 0 :
            print("Invalid Input try again!")
            Signin.withdrawCredit(self)
        else:
            with open(f"{self.username}Credit","r") as file:
                for line in file:
                    stored_username,stored_password,stored_value = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        # self.value = int(amt) + int(stored_value)
                        with open(f"{self.username}Credit","w") as file:
                            self.value = int(amt) + int(stored_value)
                            file.write(f"{self.username},{self.password},{self.value}\n")
                            file.close()
                        return
            file.close()

    print("-----------------------------Welcome-----------------------")
    print("Hello bro/sis")

class All:
    def all(self):
        print("1.signin\n2.signup\n3.exit")
        number = int(input("Enter a number: "))

        match number:
            case 1:
                # Signin.login(self)
                x = Signin()
                x.login()
            case 2:
                # Signup.register(self)
                x = Signup()
                x.register()
            case 3:
                exit
            case _:
                print("Please follow the above guide")
                all()

x = All()
x.all()