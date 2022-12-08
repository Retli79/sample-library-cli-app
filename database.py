import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from connect import connect
import psycopg2
from config import config
import datetime

console = Console()
app = typer.Typer()




def signup(username: str):    
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"""INSERT INTO  public.users (user_name) VALUES ('{username}')"""
    cur.execute(sql)
    conn.commit()
    

def users():
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"""SELECT * FROM  users """

    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    return users

def show_users(users):
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("#", style="dim", width=3, justify="center")   
    table.add_column("User ID", style="dim", min_width=10, justify="center")
    table.add_column("User Name", style="dim", min_width=10, justify="center")
    
    for idx, user in enumerate(users, start=1):
        table.add_row(f'[bold blue]{str(idx)}[/bold blue]',f'[cyan]{str(user[0])}[/cyan]',f'[green]{str(user[1])}[/green]')
    console.print(table)


def remove_user(username: str):    
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" DELETE FROM public.users where user_name = ('{username}')  """
    cur.execute(sql)
    conn.commit()



def add(book_name: str, author_name:str, pages:int, genre:str, availability:bool ):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"""INSERT INTO  public.book (book_name, author_name, pages, genre, availability) 
            VALUES ('{book_name}', '{author_name}', {pages}, '{genre}', '{availability}');
                     
            """
    cur.execute(sql)
    conn.commit()

def books():
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f"""SELECT * FROM  book """

    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books


def show_books(books):


    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("#", style="dim", width=3, justify="center")  
    table.add_column("Book ID", style="dim", min_width=1, justify="center")
    table.add_column("Book Name", style="dim", min_width=10, justify="center")
    table.add_column("Author", style="dim", min_width=10, justify="center")
    table.add_column("Pages", style="dim", min_width=4, justify="center")
    table.add_column("Genre", style="dim", min_width=10, justify="center")
    table.add_column("Availability", style="dim", min_width=10, justify="center")
    table.add_column("Date_added", style="dim", min_width=10, justify="center")
    

    for idx, book in enumerate(books, start=1):
        table.add_row(f'[bold blue]{str(idx)}[/bold blue]', f'[cyan]{str(book[0])}[/cyan]',f'[green]{str(book[1])}[/green]', 
        f'[green]{str(book[2])}[/green]', f'[green]{str(book[3])}[/green]', 
        f'[green]{str(book[4])}[/green]', f'[green]{str(book[5])}[/green]', 
        f'[green]{str(book[6])}[/green]')

    console.print(table)
    
    

    


def delete(book_id):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" DELETE FROM public.book where book_id = ('{book_id}')"""
    cur.execute(sql)
    conn.commit()


def update(book_id:int, book_name: str, author_name:str, pages:int, genre:str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" UPDATE book SET book_name = ('{book_name}') , author_name = ('{author_name}')
               , pages = ('{pages}') , genre = ('{genre}')
                WHERE book_id = ('{book_id}')
         """
    cur.execute(sql)
    conn.commit()


def get_books(user_name = str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" 
               SElECT user_name, * FROM book 
               join command on book.book_id = command.book_id
               join users on users.user_id = command.user_id 
               where user_name = ('{user_name}') 

         """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books


def fav_books(user_name = str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" 
               SElECT users.user_name , * FROM book JOIN command ON book.book_id = command.book_id 
               join users on users.user_id = command.user_id
               WHERE user_name = ('{user_name}')  and fav_book = true;
               
         """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books





def display_table(books):


    table = Table(show_header=True, header_style="bold blue", show_lines=True)
   
    table.add_column("User Name", style="dim", min_width=1, justify="center")
    table.add_column("Book ID", style="dim", min_width=1, justify="center")
    table.add_column("Book Name", style="dim", min_width=10, justify="center")
    table.add_column("Author", style="dim", min_width=10, justify="center")
    table.add_column("Pages", style="dim", min_width=4, justify="center")
    table.add_column("Genre", style="dim", min_width=10, justify="center")
    table.add_column("Availability", style="dim", min_width=10, justify="center")
    table.add_column("Date_added", style="dim", min_width=10, justify="center")


    for book in books:
        table.add_row(f'[cyan]{str(book[0])}[/cyan]',f'[green]{str(book[1])}[/green]', 
        f'[green]{str(book[2])}[/green]', f'[green]{str(book[3])}[/green]', 
        f'[green]{str(book[4])}[/green]', f'[green]{str(book[5])}[/green]', 
        f'[green]{str(book[6])}[/green]',f'[green]{str(book[7])}[/green]')
    
    

    console.print(table)


def get_statistics(user_name = str):
    conn = psycopg2.connect("dbname=Group2DB user=postgres password=postgres")
    cur = conn.cursor()
    sql = f""" 
               SELECT  count(C.mark_read), count(distinct(B.author_name)), count(distinct(B.genre)), sum(B.pages) from command AS  C 
                INNER JOIN users AS U  ON u.user_id = c.user_id
                INNER JOIN book AS B ON b.book_id = c.book_id where mark_read is true and u.user_name = ('{user_name}')
  
               
         """
    cur.execute(sql)
    counts = cur.fetchall()
    conn.commit()
    return counts


def display_statistics(counts):
    
    
    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Statistics", style="dim", width=30, justify= "center")
    table.add_column("Numbers", style="dim", min_width=10, justify= "center")
    table.add_row('Books you read', str(counts[0][0]))
    table.add_row('Author you read', str(counts[0][1]))
    table.add_row('Genre you read', str(counts[0][2]))
    table.add_row('Total pages you read', str(counts[0][3]))
    console.print(table)
    



   
        

    








  
    
