from tkinter import *

'''
class MakeWindow(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side = "top",
                       fill = "both",
                       expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, LogInMenu, SignUpMenu, MainMenu, PWHall):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
'''


# Button functionality


def button_func(f):
    clear_all_frames()
    f.pack()


def addactfunc():

    global count

    acc_card = Button(
        parent_pwhall,
        image=add_acc,
        border=0
    )
    acc_card.grid(row=1 + count // 5, column=count % 5, padx=10, pady=20)

    count += 1


def clear_all_frames():
    parent_mainmenu.pack_forget()
    parent_login.pack_forget()
    parent_signup.pack_forget()


window = Tk()
window.title("PassManage")
window.geometry("1920x1080+1+1")

# Main menu


# image definition

photo = PhotoImage(file=r"C:\Users\Rishabh Chopde\Desktop\Unimportant pictures\momo4.png")
add_acc = PhotoImage(file=r"C:\Users\Rishabh Chopde\PycharmProjects\pwmanager\GUI sources\add_acc.png")
top_bar_img = PhotoImage(file=r"C:\Users\Rishabh Chopde\PycharmProjects\pwmanager\GUI sources\top_bar.png")

# Main menu widgets

parent_mainmenu = Frame(window, width=1920, height=1080)
parent_mainmenu.pack()

label_space = Label(
    parent_mainmenu,
    text="\n\n"
)
label_space.pack()

logo = Label(
    parent_mainmenu,
    image=photo
)
logo.pack()

welcome = Label(
    parent_mainmenu,
    text="WELCOME!",
    width=10,
    font=('Futura XBlk BT', 50, "bold", "italic")
)
welcome.pack()

login_btn = Button(
    parent_mainmenu,
    text="Log In",
    font="times 40",
    width=7,
    command=lambda: button_func(parent_login)
)
login_btn.pack(pady=10)

signup_btn = Button(
    parent_mainmenu,
    text="Sign Up",
    font="times 40",
    command=lambda: button_func(parent_signup)
)
signup_btn.pack()

# Log In menu


parent_login = Frame(window, width=1920, height=1080)

label_space2 = Label(
    parent_login,
    text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
)
label_space2.grid(row=0, column=0, columnspan=2, padx=650)

username = Label(
    parent_login,
    text="Username:                                                  ",
    font=("Lucida Sans", 20)
)
username.grid(row=1, column=0, columnspan=2, padx=650)

e_username = Entry(
    parent_login,
    width=26,
    border=0,
    bg="yellow",
    font=('Comic Sans MS', 30)
)
e_username.grid(row=2, column=0, columnspan=2, padx=650)

password = Label(
    parent_login,
    text="Password:                                                  ",
    font=("Lucida Sans", 20)
)
password.grid(row=3, column=0, columnspan=2, padx=650)

e_password = Entry(
    parent_login,
    width=26,
    border=0,
    bg="yellow",
    font=('Comic Sans MS', 30)
)
e_password.grid(row=4, column=0, columnspan=2, padx=650)

sign_up = Button(
    parent_login,
    command=lambda: button_func(parent_signup),
    text="Don't have an account? Sign up for free!",
    font=("Comic Sans MS", 10),
    border=0
)
sign_up.grid(row=5, column=0, columnspan=2, padx=50, pady=5)

go_back = Button(
    parent_login,
    text="Go back",
    command=lambda: button_func(parent_mainmenu),
    font=('Futura XBlk BT', 30),
    width=10
)
go_back.grid(row=6, column=0, padx=20, pady=5, sticky="e")

log_Into = Button(
    parent_login,
    text="Log in",
    command=lambda: button_func(parent_pwhall),
    font=('Futura XBlk BT', 30),
    width=10
)
log_Into.grid(row=6, column=1, padx=20, pady=5, sticky="w")

# Sign Up menu layout


parent_signup = Frame(window, width=1920, height=1080)

label_space = Label(
    parent_signup,
    text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
)
label_space.grid(row=0, column=0, columnspan=2, padx=650)

username = Label(
    parent_signup,
    text="Username:                                                   ",
    font=("Lucida Sans", 20)
)
username.grid(row=1, column=0, columnspan=2, padx=650, pady=10)

e_username = Entry(
    parent_signup,
    width=26,
    border=0,
    bg="yellow",
    font=('Comic Sans MS', 30)
)
e_username.grid(row=2, column=0, columnspan=2, padx=650)

password = Label(
    parent_signup,
    text="Password:                                                    ",
    font=("Lucida Sans", 20)
)
password.grid(row=3, column=0, columnspan=2, padx=650, pady=10)

e_password = Entry(
    parent_signup,
    width=26,
    border=0,
    bg="yellow",
    font=('Comic Sans MS', 30)
)
e_password.grid(row=4, column=0, columnspan=2, padx=650)

reenter = Label(
    parent_signup,
    text="Re-enter password:                                       ",
    font=("Lucida Sans", 20)
)
reenter.grid(row=5, column=0, columnspan=2, padx=650, pady=10)

re_password = Entry(
    parent_signup,
    width=26,
    border=0,
    bg="yellow",
    font=('Comic Sans MS', 30)
)
re_password.grid(row=6, column=0, columnspan=2, padx=650)

log_in = Button(
    parent_signup,
    command=lambda: button_func(parent_login),
    text="Have an account? Log in!",
    font=("Comic Sans MS", 10),
    border=0
)
log_in.grid(row=7, column=0, columnspan=2, padx=50, pady=5)

go_back = Button(
    parent_signup,
    text="Go back",
    command=lambda: button_func(parent_mainmenu),
    font=('Futura XBlk BT', 30),
    width=10
)
go_back.grid(row=8, column=0, padx=20, pady=5, sticky="e")

sign_upto = Button(
    parent_signup,
    text="Sign Up",
    font=('Futura XBlk BT', 30),
    width=10
)
sign_upto.grid(row=8, column=1, padx=20, pady=5, sticky="w")

# Password hall menu


count = 1

parent_pwhall = Frame(window, width=1920, height=1080)

top_bar = Label(
    parent_pwhall,
    image=top_bar_img,
    height=200
)
top_bar.grid(row=0, column=0, columnspan=count)

add_acc_button = Button(
    parent_pwhall,
    command=addactfunc(),
    image=add_acc,
    border=0
)
add_acc_button.grid(row=1, column=0, padx=10, pady=20)

window.mainloop()
