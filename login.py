from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql


def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required',parent=window)
        elif newpass_entry.get()!=confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm password are not matching',parent=window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='FLowers*11',database='book_paradise')
            cur=con.cursor()
            query='select * from signup where username=%s'
            cur.execute(query,(user_entry.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update signup set password=%s where username=%s'
                cur.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password',parent=window)
                window.destroy()

    window=Toplevel()
    window.title('Change Password')

    bgPic=ImageTk.PhotoImage(file='background.jpg')
    bglabel=Label(window,image=bgPic)
    bglabel.grid()

    heading_label=Label(window,text='RESET PASSWORD',font=('arial',18,'bold'),bg='white',fg='magenta2')
    heading_label.place(x=480,y=60)

    userLabel=Label(window,text='Username',font=('arial',12,'bold'),bg='white',fg='orchid1')
    userLabel.place(x=470,y=130)

    user_entry=Entry(window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    user_entry.place(x=470,y=160)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=180)

    passwordLabel=Label(window,text='New Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    passwordLabel.place(x=470,y=210)

    newpass_entry=Entry(window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    newpass_entry.place(x=470,y=240)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=260)

    confirmpassLabel=Label(window,text='Confirm Password',font=('arial',12,'bold'),bg='white',fg='orchid1')
    confirmpassLabel.place(x=470,y=290)

    confirmpass_entry=Entry(window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=0)
    confirmpass_entry.place(x=470,y=320)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=340)

    submitButton=Button(window,text='Submit',bd=0,bg='magenta2',fg='white',font=('Open Sans',16,'bold'),width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',command=change_password)
    submitButton.place(x=470,y=390)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="FLowers*11",database="book_paradise")
            cur=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query='use book_paradise'
        cur.execute(query)
        query='select * from signup where username=%s and password=%s'
        cur.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=cur.fetchone()
        if row ==None:
            messagebox.showerror('Error','Invalid username or password')
        root.destroy()
        #import mainpage



def signup_page():
    root.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

root=Tk()
root.geometry('990x660+50+50')
root.resizable(0,0)
root.title('Login Page')

bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

heading=Label(root,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

usernameEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(root,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

passwordEntry=Entry(root,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'Password')

passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(root,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(root,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(root,text='Forgot Password?',font=('Microsoft Yahei UI Light',9,'bold'),fg='firebrick1',activeforeground='firebrick1',bd=0,bg='white',activebackground='white',cursor='hand2',command=forget_pass)
forgetButton.place(x=715,y=295)

loginButton=Button(root,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)

orLabel=Label(root,text='-------------- OR --------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(root,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(root,image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(root,image=twitter_logo,bg='white')
twitterLabel.place(x=740,y=440)

signupLabel=Label(root,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=570,y=500)

newaccountButton=Button(root,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=727,y=500)

root.mainloop()