import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from connect import connect
import psycopg2
from config import config
import datetime
from database import *


console = Console()
app = typer.Typer()


@app.command("start")
def start():
    typer.secho(f'''Welcome to Library CLI!\n\n
        You can execute command '--help' to see the possible commands''', fg=typer.colors.GREEN)
    connect()


@app.command("sign_up")
def sign_up():
    username = input('Enter your username: ')
    typer.echo(f"Nice that {username} are signing up!")
    signup(username)
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



    
    

if __name__ == "__main__":
    app()
    

