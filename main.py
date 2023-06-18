import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from connect import connect
from database import *


console = Console()
app = typer.Typer()

# Establish a connection
conn = connect()


@app.command("start")
def start():
    typer.secho(f'''Welcome to Library CLI!\n\n
        You can execute command '--help' to see the possible commands''', fg=typer.colors.GREEN)
   


@app.command("sign_up")
def sign_up():
    username = input('Enter your username: ')
    typer.echo(f"Nice that {username} are signing up!")
    signup(username)
    

@app.command("display_users")
def display_users():
     typer.echo(f"All users")
     show_users(users())
     
    

@app.command("delete_user")
def delete_user():
    username = input('Enter your username: ')
    typer.echo(f"{username} is removed!")
    remove_user(username)
    show_users(users())


@app.command("add_book")
def add_book():    
    bookname = input('Enter a book name: ')
    authorname = input('Enter a author name: ')
    pagesbook = input('Enter pages: ')
    genrebook = input('Enter a genre: ')
    availabilities =  input('Enter true: ')      
    add(bookname, authorname, pagesbook, genrebook, availabilities)
    typer.echo(f"{bookname} is added!")
    show_books(books())

    

@app.command("delete_book")
def delete_book():
    bookid = input('Enter a book ID: ')
    delete(bookid)
    typer.echo(f"Book is deleted!")
    show_books(books())


@app.command("update_book")
def update_book():
    bookid = input('Enter a book ID: ')
    bookname = input('Enter a book name: ')
    authorname = input('Enter a author name: ')
    pagesbook = input('Enter pages: ')
    genrebook = input('Enter a genre: ')
    update(bookid,bookname,authorname, pagesbook,genrebook  ) 
    typer.echo(f" {bookname} is updated!")
    show_books(books())
     


@app.command("get_book")
def get_book():
    username = input('Enter your username: ')
    typer.echo(f"{username}`books are displayed!")
    display_table(get_books(username))
   


@app.command("fav_book")
def fav_book():
    username = input('Enter your username: ')
    typer.echo(f"Favorite books are displayed!")
    display_table(fav_books(username))



@app.command("statistics")
def statistics():
    username = input('Enter your username: ')
    typer.echo(f"Statistics are displayed!")
    display_statistics(get_statistics(username))




@app.command("search_by_name")
def search_by_name(name:str):
       typer.echo(f"Books are displayed!")
       books= search_name(name)
       display_table(books)


@app.command("search_by_author")
def search_by_author(author:str):
       typer.echo(f"Books are displayed!")
       books= search_author(author)
       display_table(books)


@app.command("recently_added")
def recently_added(author: Optional[str]= typer.Argument("")):
       typer.echo(f"Books are displayed!")
       books= recent_added(author)
       display_table(books)


@app.command("most_read_books")
def most_read_books(genre: Optional[str]= typer.Argument("")):
       typer.echo(f"Books are displayed!")
       books= mostread_books(genre)
       print(books)
       table = Table(show_header=True, header_style="bold blue")
       table.add_column("Book ID", style="dim", min_width=10, justify=True)
       table.add_column("Book Name", style="dim", min_width=10, justify=True)
       table.add_column("Author", style="dim", min_width=10, justify=True)
       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), book[1], book[2], str(book[3]), str(book[4]))
       console.print(table)



@app.command("most_favorite_books")
def most_favorite_books(genre: Optional[str]= typer.Argument("")):
       typer.echo(f"Books are displayed!")
       books= most_favorite(genre)
       table = Table(show_header=True, header_style="bold blue")
       table.add_column("Book ID", style="dim", min_width=10, justify=True)
       table.add_column("Book Name", style="dim", min_width=10, justify=True)
       table.add_column("Author", style="dim", min_width=10, justify=True)
       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), book[1], book[2], str(book[3]), str(book[4]))
       console.print(table)


@app.command("most_read_genres")
def most_read_genres():
       typer.echo(f"Books are displayed!")
       books= mostread_genres()
       table = Table(show_header=True, header_style="bold blue")
       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), str(book[1]))
       console.print(table)


@app.command("most_read_authors")
def most_read_authors():
       typer.echo(f"Books are displayed!")
       books= mostread_authors()
       table = Table(show_header=True, header_style="bold blue")
       table.add_column("Genre", style="dim", min_width=10, justify=True)
       table.add_column("Count", style="dim", min_width=10, justify=True)
       for book in books:
           table.add_row(str(book[0]), str(book[1]))
       console.print(table)




@app.command("display_table")
def display_table(books):
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    table.add_column("Date", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]), str(book[6]))
        console.print(table)
    else:
        console.print(table)



@app.command("mark_read")
def mark_read(book_id: int, user_id: int):
    typer.echo(f'You marked book {book_id} as read!')
    markread(book_id,user_id)


@app.command("mark_reading")
def mark_reading(book_id:int, user_id: int):
    typer.echo(f'You marked book {book_id} as reading!')
    markreading(book_id, user_id)


@app.command("mark_will_read")
def mark_will_read(book_id: int, user_id: int):
    typer.echo(f'You marked book {book_id} as will read!')
    mark_willread(book_id, user_id)
    

@app.command("fav_book")
def fav_book(book_id: int, user_id: int):
    typer.echo(f'You added book {book_id} to your favorites!')
    fav_books(book_id, user_id)

   

@app.command("show_my_books")
def show_my_books(user_id: int):
    typer.echo("BOOKS YOU READ!")
    books = my_book_read(user_id)
    display_tables(books)

    typer.echo("BOOKS YOU ARE READING!")
    books = my_book_reading(user_id)
    display_tables(books)

    typer.echo("BOOKS YOU WILL READ!")
    books = my_book_will_read(user_id)
    display_tables(books)

    typer.echo("YOUR FAVORITE BOOKS!")
    books = my_fav_book(user_id)
    display_tables(books)
    
    

if __name__ == "__main__":
    app()


    

