from tkinter import *
from tkinter import messagebox
from database import Database

root = Tk()
root.title("LOGIN TEST")
root.geometry("500x300")

db = Database('store.db')

# Sign In
def popUp(check):
    if check == 1:
        messagebox.showinfo("Right password", "You Have entered the right password")
        return
    elif check == 0:
        messagebox.showerror("Invalid password", "Please input the right password")
        return
    
def passwordCheck(password):
    if password == passwordText.get():
        popUp(1)
    else:
        popUp(0)

def Signin():
    for user in db.fetch():
        if user[1] == usernameText.get():
            passwordCheck(user[2])
            return
    messagebox.showerror("Invalid Username", "Please input the right Username")
        
#Create
def CreateAcc():
    root.withdraw()
    top.deiconify()

def CreateButton():
    if ConfirmPasswordEntry.get() == '' or CreatePasswordEntry.get() == '':
        messagebox.showerror("fill required field", "Please fill the required field")
    elif ConfirmPasswordEntry.get() == CreatePasswordEntry.get():
        db.insert(CreateUsernameEntry.get(), CreatePasswordEntry.get())
        top.withdraw()
        root.deiconify()
    else:
        messagebox.showerror("Wrong Password", "Password didnt match")



#Sub Title
subTitleLabel = Label(root, text = "Please Input", font = ('bold',14), pady = 20,padx = 80)
subTitleLabel.grid(row = 1, column = 2)

#Username
usernameLabel = Label(root, text = "Username : ", font = ('bold',14), pady = 20)
usernameLabel.grid(row = 2, column = 1)
usernameText = StringVar()
usernameEntry = Entry(root, textvariable = usernameText)
usernameEntry.grid(row = 2,column = 2)

#Password
passwordLabel = Label(root, text = "Password : ", font = ('bold',14), pady = 20)
passwordLabel.grid(row = 3, column = 1)
passwordText = StringVar()
passwordEntry = Entry(root, textvariable = passwordText)
passwordEntry.grid(row = 3,column = 2)

#submit button
submitButton = Button(root, text = "submit", width = 12, command = Signin)
submitButton.grid(row = 4,column = 2)

#Create button
createLabel = Label(root, text = "Dont have account?Create a new one ", font = ('bold',14), pady = 20)
createLabel.grid(row = 5, column = 1, columnspan = 2)
createButton = Button(root, text = "Create", width = 12, command = CreateAcc)
createButton.grid(row = 5,column = 3)




#TOPLEVEL
top = Toplevel(root)
top.geometry("400x300")

#username
CreateUsernameLabel = Label(top, text = "Create Username : ", font = ('bold',14), pady = 20)
CreateUsernameLabel.grid(row = 0, column = 0)
CreateUsernameEntry = Entry(top)
CreateUsernameEntry.grid(row = 0,column = 1)

#Password
CreatePasswordLabel = Label(top, text = "Create Password : ", font = ('bold',14), pady = 20)
CreatePasswordLabel.grid(row = 1, column = 0)
CreatePasswordEntry = Entry(top)
CreatePasswordEntry.grid(row = 1,column = 1)

#ConfirmPassword
ConfirmPasswordLabel = Label(top, text = "Confirm Username : ", font = ('bold',14), pady = 20)
ConfirmPasswordLabel.grid(row = 2, column = 0)
ConfirmPasswordEntry = Entry(top)
ConfirmPasswordEntry.grid(row = 2,column = 1)

#Button
submitButtonCreate = Button(top, text = "Create Account", width = 12,command = CreateButton)
submitButtonCreate.grid(row = 3,column = 1, columnspan = 2)
top.withdraw()
root.mainloop()