import tkinter as tk
import random as r

root = tk.Tk()
root.title("Password Manager")
PHOTO = tk.PhotoImage(file="logo.png")
info = {"Website" : "", "Username": "", "Password": ""}

def generate_pass():
    pass_fill.delete(0, tk.END)
    passwords = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    for i in range(0, 4):
        x = r.randint(0, 51)
        passwords.append(letters[x])
        y = r.randint(0, 9)
        passwords.append(numbers[y])
        z = r.randint(0, 8)
        passwords.append(symbols[z])

    r.shuffle(passwords)
    passwords = "".join(passwords)
    pass_fill.insert(0, passwords)
    root.clipboard_clear()
    root.clipboard_append(passwords)
    info["Password"] = passwords

def send_to_data():
    with open("data.txt", "a") as path: 
        for item in info:
            path.write(f"{info[item]} | ")  
        path.write("\n")  

def create():
    def do():
        if web_fill.get() != "" and user_fill.get() != "" and pass_fill.get() != "":
            passw = pass_fill.get()
            usern = user_fill.get()
            webf = web_fill.get()
            info["Website"] = webf  
            info["Username"] = usern
            info["Password"] = passw
            send_to_data()
            popup.destroy()
        else:
            popup.destroy()
            popup2 = tk.Toplevel(root)
            popup2.title("Oops")
            popup2.geometry("300x200")
            label2 = tk.Label(popup2, text="Please don't leave ANY fields empty!")
            close = tk.Button(popup2, text="Ok", command=popup2.destroy, bg="#008CBA", fg="white", relief="raised", font=("Arial", 10))
            label2.grid(row=0, column=0, columnspan=2, pady=20)
            close.grid(row=1, column=0, columnspan=2, pady=10)

    popup = tk.Toplevel(root)
    popup.title("Are you Sure?")
    popup.geometry("300x200")
    label = tk.Label(popup, text="ARE YOU SURE?", font=("Arial", 12, "bold"))
    no = tk.Button(popup, text="No", command=popup.destroy, bg="#f44336", fg="white", relief="raised", font=("Arial", 10))
    yes = tk.Button(popup, text="Yes", command=do, bg="#4CAF50", fg="white", relief="raised", font=("Arial", 10))
    
    label.grid(row=0, column=0, columnspan=2, pady=20)
    no.grid(row=1, column=0, padx=10, pady=10)
    yes.grid(row=1, column=1, padx=10, pady=10)

def clears():
    with open("data.txt", "w") as path: 
        pass 

canva = tk.Canvas(root, width=200, height=224)
canva.create_image(100, 112, image=PHOTO)

website = tk.Label(root, text="Website: ")
web_fill = tk.Entry(root, width=35)
 
user = tk.Label(root, text="Email/Username: ")
user_fill = tk.Entry(root, width=35)

password = tk.Label(root, text="Password: ")
pass_fill = tk.Entry(root, width=35)

generate = tk.Button(root, text="Generate Password", command=generate_pass, width=20, bg="#4CAF50", fg="white", relief="raised", font=("Arial", 10))
add = tk.Button(root, text="Add", command=create, width=20, bg="#008CBA", fg="white", relief="raised", font=("Arial", 10))
clear = tk.Button(root, text='CLEAR ALL PASSWORDS', command=clears, width=20, bg="#f44336", fg="white", relief="raised", font=("Arial", 10))

canva.grid(row=0, column=0, columnspan=3, pady=20)

website.grid(row=1, column=0, padx=10, pady=5, sticky="e")
web_fill.grid(row=1, column=1, columnspan=2, pady=5)

user.grid(row=2, column=0, padx=10, pady=5, sticky="e")
user_fill.grid(row=2, column=1, columnspan=2, pady=5)

password.grid(row=3, column=0, padx=10, pady=5, sticky="e")
pass_fill.grid(row=3, column=1, columnspan=2, pady=5)

generate.grid(row=4, column=0, columnspan=3, pady=10)
add.grid(row=5, column=0, columnspan=3, pady=10)
clear.grid(row=6, column=0, columnspan=3, pady=20)

root.mainloop()
