import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from connect import connect
from database import *



console = Console()
app = typer.Typer()





def signup(username: str):    
    conn = connect()
    cur = conn.cursor()
    sql = f"""INSERT INTO  public.users (user_name) VALUES ('{username}')"""
    cur.execute(sql)
    conn.commit()
   

 

def users():
    conn = connect()
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
    conn = connect()
    cur = conn.cursor()
    sql = f""" DELETE FROM public.users where user_name = ('{username}')  """
    cur.execute(sql)
    conn.commit()



def add(book_name: str, author_name:str, pages:int, genre:str, availability:bool ):
    conn = connect()
    cur = conn.cursor()
    sql = f"""INSERT INTO  public.book (book_name, author_name, pages, genre, availability) 
            VALUES ('{book_name}', '{author_name}', {pages}, '{genre}', '{availability}');
                     
            """
    cur.execute(sql)
    conn.commit()

def books():
    conn = connect()
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
    conn = connect()
    cur = conn.cursor()
    sql = f""" DELETE FROM public.book where book_id = ('{book_id}')"""
    cur.execute(sql)
    conn.commit()


def update(book_id:int, book_name: str, author_name:str, pages:int, genre:str):
    conn = connect()
    cur = conn.cursor()
    sql = f""" UPDATE book SET book_name = ('{book_name}') , author_name = ('{author_name}')
               , pages = ('{pages}') , genre = ('{genre}')
                WHERE book_id = ('{book_id}')
         """
    cur.execute(sql)
    conn.commit()


def get_books(user_name = str):
    conn = connect()
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
    conn = connect()
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
    conn = connect()
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
    



   #####################################################################################
   ###Ghassan`s part


def search_name(name: str):
    conn = connect()
    cur = conn.cursor()
    sql = f""" SELECT * FROM public.book where book_name = '{name}' """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books
def search_author(author: str):
    conn = connect()
    cur = conn.cursor()
    sql = f""" SELECT * FROM public.book where author_name = '{author}'  """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books

def recent_added(author):
    list=[]
    conn = connect()
    cur = conn.cursor()
    sql = f""" SELECT author_name FROM public.book   """
    cur.execute(sql)
    authors = cur.fetchall()
    r= len((authors))
    for i in range(r):
         list.append(authors[i][0])


    if bool(author) is True:
        if author in list:
            conn = connect()
            cur = conn.cursor()
            sql = f""" SELECT * FROM public.book where author_name = '{author}'order by book_date_added desc limit 5
                 """
            cur.execute(sql)
            books = cur.fetchall()
            conn.commit()
            return books
        else:
            print("author does not exist!")


    elif bool(author) is False:
        conn = connect()
        cur = conn.cursor()
        sql = f""" SELECT * FROM public.book order by book_date_added desc limit 5
                     """
        cur.execute(sql)
        books = cur.fetchall()
        conn.commit()
        return books

def mostread_books(genre):
    list=[]
    conn = connect()
    cur = conn.cursor()
    sql = f""" SELECT genre FROM public.book 
                 """
    cur.execute(sql)
    genres = cur.fetchall()
    r= len((genres))
    for i in range(r):
         list.append(genres[i][0])


    if bool(genre) is True:
        if genre in list:
            conn = connect()
            cur = conn.cursor()
            sql = f"""select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
where genre = '{genre}' order by c.count desc limit 10
                 """
            cur.execute(sql)
            books = cur.fetchall()
            conn.commit()
            return books
        else:
            print("genre does not exist!")


    elif bool(genre) is False:
        conn = connect()
        cur = conn.cursor()
        sql = f""" select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
order by c.count desc limit 10
                     """
        cur.execute(sql)
        books = cur.fetchall()
        conn.commit()
        return books

def most_favorite(genre):
    list=[]
    conn = connect()
    cur = conn.cursor()
    sql = f""" SELECT genre FROM public.book   """
    cur.execute(sql)
    genres = cur.fetchall()
    r= len((genres))
    for i in range(r):
         list.append(genres[i][0])


    if bool(genre) is True:
        if genre in list:
            conn = connect()
            cur = conn.cursor()
            sql = f"""select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(fav_book) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
where genre = '{genre}' order by c.count desc limit 10
                 """
            cur.execute(sql)
            books = cur.fetchall()
            conn.commit()
            return books
        else:
            print("genre does not exist!")


    elif bool(genre) is False:
        conn = connect()
        cur = conn.cursor()
        sql = f""" select b.book_id, b.book_name, b.author_name,b.genre, c.count
from public.book as b
join (SELECT book_id, count(fav_book) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id 
order by c.count desc limit 10
                     """
        cur.execute(sql)
        books = cur.fetchall()
        conn.commit()
        return books

def mostread_genres():

    conn = connect()
    cur = conn.cursor()
    sql = f"""select b.genre, sum(c.count)
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id
GROUP BY genre order by sum desc limit 5
                 """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books
def mostread_authors():

    conn = connect()
    cur = conn.cursor()
    sql = f"""select b.author_name, sum(c.count)
from public.book as b
join (SELECT book_id, count(mark_read) FROM command GROUP BY book_id) as c
on b.book_id = c.book_id
GROUP BY author_name order by sum desc limit 5
                 """
    cur.execute(sql)
    books = cur.fetchall()
    conn.commit()
    return books

def mark_read(book_id,username):
    conn = connect()
    cur = conn.cursor()
    sql = f"INSERT INTO  public.command (mark_read) VALUES ('True') where "
    cur.execute(sql)
    conn.commit()




 #####################################################################################
   ###Rumeysa`s part
def markread(book_id: int, user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql = f""" 
        INSERT INTO public.command (book_id, user_id, mark_read) VALUES ({book_id}, {user_id}, 'True'); 
        """

    cur.execute(sql)
    conn.commit()

def markreading(book_id: int, user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql = f""" 
        INSERT INTO public.command (book_id, user_id, mark_reading) VALUES ({book_id}, {user_id}, 'True');
        """

    cur.execute(sql)
    conn.commit()

def mark_willread(book_id: int, user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql = f""" 
        INSERT INTO public.command (book_id, user_id, mark_will_read) VALUES ({book_id}, {user_id}, 'True');
        """
    cur.execute(sql)
    conn.commit()

def fav_books(book_id: int, user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql = f""" 
        INSERT INTO public.command (book_id, user_id, fav_book) VALUES ({book_id}, {user_id}, 'True');
        """
    try:    
        cur.execute(sql)
        conn.commit()
    except:
        sql = f""" 
        UPDATE public.command SET fav_book = 'True' 
        WHERE book_id = {book_id} and user_id = {user_id}
        """
        cur.execute(sql)
        conn.commit()

def my_book_read(user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql1 = f"""
        SELECT 
                command.book_id,
                book_name,
                author_name,
                pages,
                genre,
                availability
        FROM command 
        INNER JOIN book ON command.book_id = book.book_id
        WHERE mark_read = 'True' and user_id= ('{user_id}')
        """
    cur.execute(sql1)
    books = cur.fetchall()
    conn.commit()
    return books

def my_book_reading(user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql1 = f"""
        SELECT 
                command.book_id,
                book_name,
                author_name,
                pages,
                genre,
                availability
        FROM command 
        INNER JOIN book ON command.book_id = book.book_id
        WHERE mark_reading = 'True' and user_id= ('{user_id}')
        """
    cur.execute(sql1)
    books = cur.fetchall()
    conn.commit()
    return books

def my_book_will_read(user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql1 = f"""
        SELECT 
                command.book_id,
                book_name,
                author_name,
                pages,
                genre,
                availability
        FROM command 
        INNER JOIN book ON command.book_id = book.book_id
        WHERE mark_will_read = 'True' and user_id= ('{user_id}')
        """
    cur.execute(sql1)
    books = cur.fetchall()
    conn.commit()
    return books

def my_fav_book(user_id: int):
    conn = connect()
    cur = conn.cursor()
    sql1 = f"""
        SELECT 
                command.book_id,
                book_name,
                author_name,
                pages,
                genre,
                availability
        FROM command 
        INNER JOIN book ON command.book_id = book.book_id
        WHERE fav_book = 'True' and user_id= ('{user_id}')
        """
    cur.execute(sql1)
    books = cur.fetchall()
    conn.commit()
    return books




def my_books(user_id: int):
    typer.echo("BOOKS YOU READ!")
    books = my_book_read(user_id)
    table = Table(show_header=True, header_style="bold blue")

    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]))
        console.print(table)
    else:
        console.print(table)

    typer.echo("BOOKS YOU ARE READING!")
    books = my_book_reading(user_id)
    table = Table(show_header=True, header_style="bold blue")

    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]))
        console.print(table)
    else:
        console.print(table)

    typer.echo("BOOKS YOU WILL READ!")
    books = my_book_will_read(user_id)
    table = Table(show_header=True, header_style="bold blue")

    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]))
        console.print(table)
    else:
        console.print(table)

    typer.echo("YOUR FAVORITE BOOKS!")
    books = my_fav_book(user_id)
    table = Table(show_header=True, header_style="bold blue")

    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]))
        console.print(table)
    else:
        console.print(table)


def display_tables(books):
    table = Table(show_header=True, header_style="bold blue")

    table.add_column("Book ID", style="dim", min_width=10, justify=True)
    table.add_column("Book Name", style="dim", min_width=10, justify=True)
    table.add_column("Author", style="dim", min_width=10, justify=True)
    table.add_column("Pages", style="dim", min_width=10, justify=True)
    table.add_column("Genre", style="dim", min_width=10, justify=True)
    table.add_column("Availability", style="dim", min_width=10, justify=True)
    if bool(books) is True:
        for book in books:
            table.add_row(str(book[0]),str(book[1]), str(book[2]), str(book[3]), str(book[4]), str(book[5]))
        console.print(table)
    else:
        console.print(table)

    








  
    
