from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from login import *
#from signup import login_page


mypass = "root"
mydatabase="book_paradise"

con = pymysql.connect(host="localhost",user="root",password="FLowers*11",
                      database="book_paradise")
cur = con.cursor()


def search_books():
    # Get search term from entry widget
    search_term = search_entry.get()

    # Search for books matching the search term
    search_query = f"SELECT books.bid, books.title, books.author, GROUP_CONCAT(book_websites.website SEPARATOR ', ') AS websites " \
                   f"FROM books " \
                   f"LEFT JOIN book_websites ON books.bid = book_websites.bid " \
                   f"WHERE books.title LIKE '%{search_term}%' OR books.author LIKE '%{search_term}%' " \
                   f"GROUP BY books.bid"
    cur.execute(search_query)
    results = cur.fetchall()

    if results:
        # Display search results in a pop-up window
        search_results = ""
        for result in results:
            book_id, title, author, websites = result
            search_results += f"Book ID: {book_id}\nTitle: {title}\nAuthor: {author}\nWebsites: {websites}\n\n"
        messagebox.showinfo("Search Result", search_results)
    else:
        messagebox.showinfo("No Results", "No books found matching the search term.")


root = Tk()
root.title("Book Paradise")
root.minsize(width=400,height=400)
root.geometry("1100x700")

same=True
n=0.35

# Adding a background image
background_image = ImageTk.PhotoImage(file='lib.jpg')
bgLabel=Label(root,image=background_image)
bgLabel.place(x=0,y=0)


Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = background_image)
Canvas1.config(bg="white",width = 5013, height = 4634)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Book Paradise", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

search_entry = Entry(root, font=("Arial", 12))
search_entry.place(relx=0.23, rely=0.3, relwidth=0.45, relheight=0.05)

search_button = Button(root, text="Search", bg='black', fg='white', command=search_books)
search_button.place(relx=0.68, rely=0.3, relwidth=0.1, relheight=0.05)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

root.mainloop()

