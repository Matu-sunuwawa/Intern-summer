import os

class Signup:
    def __init__(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
    def register(self):
        try:
            print("-------------------Registration Page-------------------")

            f1 = open(f"{self.username}","x")

            u = ' '.join(format(ord(x), 'b') for x in self.username)
            p =' '.join(format(ord(x), 'b') for x in self.password)


            with open(f"{self.username}","a") as file:
                file.write(f'{u},{p}\n')
            
            print("Registration Successful!")
            print("")
            x = Signin()
            x.login()
        except:
            print("There are problem, be sure be safe!!")

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
                    u = ''.join(chr(int(stored_username[i*8:i*8+8],2)) for i in range(len(stored_username)//7))
                    p = ''.join(chr(int(stored_password[i*8:i*8+8],2)) for i in range(len(stored_password)//7))
                    if self.username == u and self.password == p:
                        print("It is Ok!")
                        Signin.select(self)
            print("")
        except:
            print("There is no such file or you may miss the wright username or password information!\nPlease be register!")
            All.all(self)
    
    def select(self):

        try:
            print("What are you looking for?\n1.CreateNote\n2.ReadNote\n3.UpdateNote\n4.DeleteNote\n5.go back\nchoose: ",end = '')
            note = int(input(""))
            match note:
                case 1:
                    Signin.createnote(self)
                case 2:
                    Signin.readnote(self)
                case 3:
                    Signin.updatenote(self)
                case 4:
                    Signin.deletenote(self)
                case 5:
                    All.all(self)
                case _:
                    print("Please enter the correct choice!!!")
                    pass
        except:
            print("There are problem, be sure be safe!!")
                
    def createnote(self):

        try:
            choose = input("Do you want to create new note(Y/N)?")
            i = 1
            match choose:
                case "y":
                    try:
                        f1 = open(f"{self.username}Notetake{i}.txt","x")

                        takenote = input("Take a note We proud of you:\n")

                        with open(f"{self.username}Notetake{i}.txt","a") as file:
                            file.write(f'{takenote}')
                    except FileExistsError:
                        # n = int(input("How many files want to take notes: "))
                        for j in range(1,100):
                            try:
                                f1 = open(f"{self.username}Notetake{i}.txt","x")

                                takenote = input("Take a note We proud of you:\n")

                                with open(f"{self.username}Notetake{i}.txt","a") as file:
                                    file.write(f'{takenote}')
                                break 
                            except FileExistsError:
                                i+=1
                        Signin.select(self)
                case "Y":
                    try:
                        f1 = open(f"{self.username}Notetake{i}.txt","x")

                        takenote = input("Take a note We proud of you:\n")

                        with open(f"{self.username}Notetake{i}.txt","a") as file:
                            file.write(f'{takenote}')
                    except FileExistsError:
                        # n = int(input("How many files want to take notes: "))
                        for j in range(1,100):
                            try:
                                f1 = open(f"{self.username}Notetake{i}.txt","x")

                                takenote = input("Take a note We proud of you:\n")

                                with open(f"{self.username}Notetake{i}.txt","a") as file:
                                    file.write(f'{takenote}')
                                break 
                            except FileExistsError:
                                i+=1
                        Signin.select(self)
                case "n":
                    Signin.select(self)
                case "N":
                    Signin.select(self)
                case _:
                    print("Please choose the correct one!!")
                    Signin.createnote(self)
        except:
            print("There are problem, be sure be safe Always!!")
        # try:
        #     f1 = open(f"{self.username}Notetake.txt","x")

        #     takenote = input("Take a note We proud of you:\n")

        #     with open(f"{self.username}Notetake.txt","a") as file:
        #         file.write(f'{takenote}')
        # except FileExistsError:
        #     print("-"*50,"\n\tThe file already exists!!\n","-"*50)
        #     Signin.select(self)
    def readnote(self):
        # try:
        #     with open(f"{self.username}Notetake{i}.txt","r") as file:
        #         for line in file:
        #             print(line)
        #             return
        #     print("")
        # except:
        #     print("There is no such file or you may miss the wright username or password information!\nPlease be register!")
        #     Signin.select(self)

        try:
            print("choose the file to view: ")
            for j in range(1,100):
                for k in range(1,100):
                    # f1 = open(f"{self.username}Notetake{i}.txt","x")
                    if os.path.exists(f"{self.username}Notetake{j}.txt") and j==k:
                        print(f"{k}.{self.username}Notetake{j}.txt\n")
                    # os.remove(f"{self.username}Notetake{i}.txt")
            
            choose = int(input("Enter the number: "))
            for j in range(1,100):
                if j==choose:
                    with open(f"{self.username}Notetake{j}.txt","r") as file:
                        for line in file:
                            print(line)
            Signin.select(self)
        except RuntimeError:
            print("There is problem!!!")

    def updatenote(self):
        try:
            print("choose the file to view: ")
            for j in range(1,100):
                for k in range(1,100):
                    # f1 = open(f"{self.username}Notetake{i}.txt","x")
                    if os.path.exists(f"{self.username}Notetake{j}.txt") and j==k:
                        print(f"{k}.{self.username}Notetake{j}.txt\n")
                    # os.remove(f"{self.username}Notetake{i}.txt")
            
            choose = int(input("Enter the number: "))
            for j in range(1,100):
                if j==choose:
                    with open(f"{self.username}Notetake{j}.txt","r") as file:
                        for line in file:
                            print(line,end = '')
                    newnote = line
                    new = input("")
                    with open(f"{self.username}Notetake{j}.txt","w") as file:
                        file.write(f"{newnote}{new}")
            
            Signin.select(self)
        except RuntimeError:
            print("There is problem!!!")
    
    def deletenote(self):
        try:
            
            def newdelete():
                print("choose what you want to delete:\n1.file\n2.notes in file")
                number = int(input("Enter the number: "))
                match number:
                    case 1:
                        print("choose the file to view: ")
                        for j in range(1,100):
                            for k in range(1,100):
                                # f1 = open(f"{self.username}Notetake{i}.txt","x")
                                if os.path.exists(f"{self.username}Notetake{j}.txt") and j==k:
                                    print(f"{k}.{self.username}Notetake{j}.txt\n")
                                # os.remove(f"{self.username}Notetake{i}.txt")
                        choose = int(input("Enter the number: "))
                        for j in range(1,100):
                            if j==choose:
                                if os.path.exists(f"{self.username}Notetake{j}.txt"):
                                    os.remove(f"{self.username}Notetake{j}.txt")
                    case 2:
                        print("choose the file to view: ")
                        for j in range(1,100):
                            for k in range(1,100):
                                # f1 = open(f"{self.username}Notetake{i}.txt","x")
                                if os.path.exists(f"{self.username}Notetake{j}.txt") and j==k:
                                    print(f"{k}.{self.username}Notetake{j}.txt\n")
                                # os.remove(f"{self.username}Notetake{i}.txt")
                        choose = int(input("Enter the number: "))
                        for j in range(1,100):
                            if j==choose:
                                with open(f"{self.username}Notetake{j}.txt") as file:
                                    file.readline()
                                with open(f"{self.username}Notetake{j}.txt","w") as file:
                                    file.write("")
                    case _:
                        print("Incorrect input!!")
                        newdelete()
                
            newdelete()
            Signin.select(self)
        except RuntimeError:
            print("There is problem!!!")
    

        
class All:
    def all(self):
        try:
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
        except:
            print("Incorrect input, be sure be safe!!!")
            All.all(self)

x = All()
x.all()