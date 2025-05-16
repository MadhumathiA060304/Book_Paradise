from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox

mypass = "root"
mydatabase = "book_paradise"

con = pymysql.connect(host="localhost", user="root", password="FLowers*11", database="book_paradise")
cur = con.cursor()

bookTable = "books"

def View():
    root = Tk()
    root.title("Book Paradise")
    root.minsize(width=400, height=500)
    root.geometry("1400x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root)
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Create Treeview with Scrollbar
    tree = ttk.Treeview(labelFrame, columns=("BID", "Title", "Author", "Websites"), show="headings")
    tree.place(relheight=1, relwidth=1)

    # Define column headings
    tree.heading("BID", text="BID")
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Websites", text="Websites")

    # Define column widths and anchor them to the center
    tree.column("BID", width=70, anchor="center")
    tree.column("Title", width=200, anchor="center")
    tree.column("Author", width=130, anchor="center")
    tree.column("Websites", width=700)

    # Create vertical scrollbar
    vsb = ttk.Scrollbar(labelFrame, orient="vertical", command=tree.yview)
    vsb.place(relx=0, rely=0, relheight=1)




    # Configure Treeview to use vertical scrollbar
    tree.configure(yscrollcommand=vsb.set)

    # Retrieve data from database and populate Treeview
    getBooksAndWebsites = """
        SELECT books.bid, books.title, books.author, GROUP_CONCAT(book_websites.website SEPARATOR ', ') AS websites 
        FROM books 
        LEFT JOIN book_websites ON books.bid = book_websites.bid 
        GROUP BY books.bid
    """
    try:
        cur.execute(getBooksAndWebsites)
        con.commit()
        for book_data in cur:
            tree.insert("", "end", values=(book_data[0], book_data[1], book_data[2], book_data[3]))
    except Exception as e:
        messagebox.showinfo("Failed to fetch files from database", str(e))

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


