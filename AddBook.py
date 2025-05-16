from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox, Label
import pymysql

def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    websites = bookInfo4.get().split(',')  # Splitting websites by comma to create a list

    insertBooks = "INSERT INTO "+bookTable+" VALUES(%s, %s, %s)"
    book_data = (bid, title, author)

    try:
        cur.execute(insertBooks, book_data)
        con.commit()
        messagebox.showinfo('Success', 'Book added successfully')
    except Exception as e:
        messagebox.showinfo('Error', f"Can't add data into Database: {str(e)}")
        return

    insertWebsites = "INSERT INTO book_websites (bid, website) VALUES (%s, %s)"
    website_data = [(bid, website.strip()) for website in websites]  # Stripping whitespace

    try:
        cur.executemany(insertWebsites, website_data)
        con.commit()
    except Exception as e:
        messagebox.showinfo('Error', f"Can't add websites into Database: {str(e)}")
        return

    root.destroy()
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Book Paradise")
    root.minsize(width=400,height=400)
    root.geometry("1100x500")

    mypass = "root"
    mydatabase="book_paradise"

    con = pymysql.connect(host="localhost",user="root",password="FLowers*11",database="book_paradise")
    cur = con.cursor()
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
    # Book Websites
    lb4 = Label(labelFrame, text="Websites (Separated by comma): ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
        
#Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()