import tkinter as  Tk
from tkinter import messagebox
from tkinter import *
from connect import connect
from database import *
import datetime


def start_command():
    messagebox.showinfo("Welcome", "Welcome to Library CLI!\n\nYou can execute command '--help' to see the possible commands")
    connect()




def sign_up_command():
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo("Sign Up", f"Nice that {username} is signing up!")
    signup(username, password)
    show_users(users())
    connect()
    show_main_menu()

root = Tk()

username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

sign_up_button = Button(root, text="Sign Up", command=sign_up_command)
sign_up_button.pack()

root.mainloop()



def delete_user_command():
    username = username_entry.get()
    messagebox.showinfo("Delete User", f"{username} is removed!")
    remove_user(username)
    show_users(users())
    show_main_menu()

def add_book_command():
    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    pagesbook = pagesbook_entry.get()
    genrebook = genrebook_entry.get()
    availabilities = availabilities_entry.get()
    add(bookname, authorname, pagesbook, genrebook, availabilities)
    messagebox.showinfo("Add Book", f"{bookname} is added!")
    show_books(books())
    show_main_menu()



def delete_book_command():
    bookid = bookid_entry.get()
    delete(bookid)
    messagebox.showinfo("Delete Book", "Book is deleted!")
    show_books(books())


def update_book_command():
    bookid = bookid_entry.get()
    bookname = bookname_entry.get()
    authorname = authorname_entry.get()
    pagesbook = pagesbook_entry.get()
    genrebook = genrebook_entry.get()
    update(bookid, bookname, authorname, pagesbook, genrebook)
    messagebox.showinfo("Update Book", f"{bookname} is updated!")
    show_books(books())

# Add the rest of the functions...

def show_main_menu():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    username_entry.focus()

root = Tk()

username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

sign_up_button = Button(root, text="Sign Up", command=sign_up_command)
sign_up_button.pack()

delete_user_button = Button(root, text="Delete User", command=delete_user_command)
delete_user_button.pack()

add_book_button = Button(root, text="Add Book", command=add_book_command)
add_book_button.pack()


root.mainloop()





# def get_book_command():
#     username = username_entry.get()
#     messagebox.showinfo("Get Book", f"{username}'s books are displayed!")
#     display_table(get_books(username))


# def fav_book_command():
#     username = username_entry.get()
#     messagebox.showinfo("Favorite Book", "Favorite books are displayed!")
#     display_table(fav_books(username))


# def statistics_command():
#     username = username_entry.get()
#     messagebox.showinfo("Statistics", "Statistics are displayed!")
#     display_statistics(get_statistics(username))


# def search_by_name_command():
#     name = name_entry.get()
#     messagebox.showinfo("Search by Name", "Books are displayed!")
#     books = search_name(name)
#     display_table(books)


# def search_by_author_command():
#     author = author_entry.get()
#     messagebox.showinfo("Search by Author", "Books are displayed!")
#     books = search_author(author)
#     display_table(books)


# def recently_added_command():
#     author = author_entry.get()
#     messagebox.showinfo("Recently Added", "Books are displayed!")
#     books = recent_added(author)
#     display_table(books)


# def most_read_books_command():
#     genre = genre_entry.get()
#     messagebox.showinfo("Most Read Books", "Books are displayed!")
#     books = mostread_books(genre)
#     table = Table(show_header=True, header_style="bold blue")
#     table.add_column("Book ID", style="dim", min_width=10, justify=True)
#     table.add_column("Book Name", style="dim", min_width=10, justify=True)
#     table.add_column("Author", style="dim", min_width=10, justify=True)
#     table.add_column("Genre", style="dim", min_width=10, justify=True)
#     table.add_column("Count", style="dim", min_width=10, justify=True)
#     for book in books:
#         table.add_row(str(book[0]), book[1], book[2], str(book[3]), str(book[4]))
#     console.print(table)


# def most_favorite_books_command():
#     genre = getregentry.get()
#     messagebox.showinfo("Most Favorite Books", "Books are displayed!")
#     books = most_favorite(genre)
#     table = Table(show_header=True, header_style="bold blue")
#     table.add_column("Book ID", style="dim", min_width=10, justify=True)
#     table.add_column("Book Name", style="dim", min_width=10, justify=True)
#     table.add_column("Author", style="dim", min_width=10, justify=True)
#     table.add_column("Genre", style="dim", min_width=10, justify=True)
#     table.add_column("Count", style="dim", min_width=10, justify=True)
#     for book in books:
#         table.add_row(str(book[0]), book[1], book[2], str(book[3]), str(book[4]))
#     console.print(table)


# def most_read_genres_command():
#     messagebox.showinfo("Most Read Genres", "Books are displayed!")
#     books = mostread_genres()
#     table = Table(show_header=True, header_style="bold blue")
#     table.add_column("Genre", style="dim", min_width=10, justify=True)
#     table.add_column("Count", style="dim", min_width=10, justify=True)
#     for book in books:
#         table.add_row(str(book[0]), str(book[1]))
#     console.print(table)


# def most_read_authors_command():
#     messagebox.showinfo("Most Read Authors", "Books are displayed!")
#     books = mostread_authors()
#     table = Table(show_header=True, header_style="bold blue")
#     table.add_column("Genre", style="dim", min_width=10, justify=True)
#     table.add_column("Count", style="dim", min_width=10, justify=True)
#     for book in books:
#         table.add_row(str(book[0]), str(book[1]))
#     console.print(table)


# def display_table_command(books):
#     table = Table(show_header=True, header_style="bold blue")
#     table.add_column("Book ID", style="dim", min_width=10, justify=True)
#     table.add_column("Book Name", style="dim", min_width=10, justify=True)
#     table.add_column("Author", style="dim", min_width=10, justify=True)
#     table.add_column("Pages", style="dim", min_width=10, justify=True)
#     table.add_column("Genre", style="dim", min_width=10, justify=True)
#     table.add_column("Availability", style="dim", min_width=10, justify=True)
#     table.add_column("Date", style="dim", min_width=10, justify=True)
#     if bool(books) is True:
#         for book in books:
#             table.add_row(str(book[0]), str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]), str(book[6]))
#         console.print(table)
#     else:
#         console.print(table)


# def mark_read_command():
#     book_id = int(bookid_entry.get())
#     user_id = int(userid_entry.get())
#     messagebox.showinfo("Mark Read", f"You marked book {book_id} as read!")
#     markread(book_id, user_id)


# def mark_reading_command():
#     book_id = int(bookid_entry.get())
#     user_id = int(userid_entry.get())
#     messagebox.showinfo("Mark Reading", f"You marked book {book_id} as reading!")
#     markreading(book_id, user_id)


# def mark_will_read_command():
#     book_id = int(bookid_entry.get())
#     user_id = int(userid_entry.get())
#     messagebox.showinfo("Mark Will Read", f"You marked book {book_id} as will read!")
#     mark_willread(book_id, user_id)


# def fav_book_command():
#     book_id = int(bookid_entry.get())
#     user_id = int(userid_entry.get())
#     messagebox.showinfo("Favorite Book", f"You added book {book_id} to your favorites!")
#     fav_books(book_id, user_id)


# def show_my_books_command():
#     user_id = int(userid_entry.get())

#     messagebox.showinfo("Your Books", "BOOKS YOU READ!")
#     books = my_book_read(user_id)
#     display_tables(books)

#     messagebox.showinfo("Your Books", "BOOKS YOU ARE READING!")
#     books = my_book_reading(user_id)
#     display_tables(books)

#     messagebox.showinfo("Your Books", "BOOKS YOU WILL READ!")
#     books = my_book_will_read(user_id)
#     display_tables(books)

#     messagebox.showinfo("Your Books", "YOUR FAVORITE BOOKS!")
#     books = my_fav_book(user_id)
#     display_tables(books)


# Creating the main window
window = Tk()
window.title("Library CLI")
window.geometry("500x400")

# Creating the labels
welcome_label = Label(window, text="Welcome to Library CLI!", font=("Arial Bold", 28))
welcome_label.pack(pady=10)

# Creating the buttons
start_button = Button(window, text="Start", command=start_command)
start_button.pack(pady=10)

sign_up_button = Button(window, text="Sign Up", command=sign_up_command)
sign_up_button.pack(pady=10)

delete_user_button = Button(window, text="Delete User", command=delete_user_command)
delete_user_button.pack(pady=10)

add_book_button = Button(window, text="Add Book", command=add_book_command)
add_book_button.pack(pady=10)

delete_book_button = Button(window, text="Delete Book", command=delete_book_command)
delete_book_button.pack(pady=10)

update_book_button = Button(window, text="Update Book", command=update_book_command)
update_book_button.pack(pady=10)

# get_book_button = Button(window, text="Get Book", command=get_book_command)
# get_book_button.pack(pady=10)

# fav_book_button = Button(window, text="Favorite Book", command=fav_book_command)
# fav_book_button.pack(pady=10)

# statistics_button = Button(window, text="Statistics", command=statistics_command)
# statistics_button.pack(pady=10)

# search_by_name_button = Button(window, text="Search by Name", command=search_by_name_command)
# search_by_name_button.pack(pady=10)

# search_by_author_button = Button(window, text="Search by Author", command=search_by_author_command)
# search_by_author_button.pack(pady=10)

# recently_added_button = Button(window, text="Recently Added", command=recently_added_command)
# recently_added_button.pack(pady=10)

# most_read_books_button = Button(window, text="Most Read Books", command=most_read_books_command)
# most_read_books_button.pack(pady=10)

# most_favorite_books_button = Button(window, text="Most Favorite Books", command=most_favorite_books_command)
# most_favorite_books_button.pack(pady=10)

# most_read_genres_button = Button(window, text="Most Read Genres", command=most_read_genres_command)
# most_read_genres_button.pack(pady=10)

# most_read_authors_button = Button(window, text="Most Read Authors", command=most_read_authors_command)
# most_read_authors_button.pack(pady=10)

# display_table_button = Button(window, text="Display Table", command=display_table_command)
# display_table_button.pack(pady=10)

# mark_read_button = Button(window, text="Mark Read", command=mark_read_command)
# mark_read_button.pack(pady=10)

# mark_reading_button = Button(window, text="Mark Reading", command=mark_reading_command)
# mark_reading_button.pack(pady=10)

# mark_will_read_button = Button(window, text="Mark Will Read", command=mark_will_read_command)
# mark_will_read_button.pack(pady=10)

# fav_book_button = Button(window, text="Favorite Book", command=fav_book_command)
# fav_book_button.pack(pady=10)

# show_my_books_button = Button(window, text="Show My Books", command=show_my_books_command)
# show_my_books_button.pack(pady=10)

# Creating the entry fields
username_label = Label(window, text="Username:")
username_label.pack(pady=5)
username_entry = Entry(window, width=30)
username_entry.pack(pady=5)

bookname_label = Label(window, text="Book Name:")
bookname_label.pack(pady=5)
bookname_entry = Entry(window, width=30)
bookname_entry.pack(pady=5)

authorname_label = Label(window, text="Author Name:")
authorname_label.pack(pady=5)
authorname_entry = Entry(window, width=30)
authorname_entry.pack(pady=5)

pagesbook_label = Label(window, text="Number of Pages:")
pagesbook_label.pack(pady=5)
pagesbook_entry = Entry(window, width=30)
pagesbook_entry.pack(pady=5)

genrebook_label = Label(window, text="Genre:")
genrebook_label.pack(pady=5)
genrebook_entry = Entry(window, width=30)
genrebook_entry.pack(pady=5)

availabilities_label = Label(window, text="Availabilities:")
availabilities_label.pack(pady=5)
availabilities_entry = Entry(window, width=30)
availabilities_entry.pack(pady=5)

bookid_label = Label(window, text="Book ID:")
bookid_label.pack(pady=5)
bookid_entry = Entry(window, width=30)
bookid_entry.pack(pady=5)

name_label = Label(window, text="Name:")
name_label.pack(pady=5)
name_entry = Entry(window, width=30)
name_entry.pack(pady=5)

author_label = Label(window, text="Author:")
author_label.pack(pady=5)
author_entry = Entry(window, width=30)
author_entry.pack(pady=5)

userid_label = Label(window, text="User ID:")
userid_label.pack(pady=5)
userid_entry = Entry(window, width=30)
userid_entry.pack(pady=5)

window.mainloop()
