master_pwd = input("What is the master password? ")

def view():
     with open("passwords.txt", "r") as f: 
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)
            


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", "a") as f: 
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing passwords (view, add)? Press q to quit. ")
    if mode.lower() == "q":
        break
    
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()
    else:
        print("Invalid mode.")
        continue
    