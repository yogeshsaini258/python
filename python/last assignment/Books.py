from dbutils import result_as_dict

def get_all_books(cursor):
    cursor.execute('select * from Books')
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def get_books_by_id(cursor,id):
    cursor.execute('select * from Books where bookid=?',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def get_books_by_authorid(cursor,a_id):
    cursor.execute('select * from Books where authorid=?',a_id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def add_book(cursor,b_id,title,details,a_id):
    cursor.execute('insert into Books(bookid,title,details,authorid) VALUES (?,?,?,?)',b_id,title,details,a_id)
    print(f'Book {b_id} added')

def remove_book(cursor,b_id):
    cursor.execute('DELETE from Books where bookid=?',b_id)
    print(f'{b_id} removed')

def get_book_review(cursor,id):
    cursor.execute('''SELECT B.title,B.details, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.bookid
                      WHERE R.reviewid = ?''',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)

def add_book_review(cursor,r_id,b_id,u_id,rating,review_text):
    cursor.execute('insert into Reviews(reviewid,bookid,userid,rating,review_text) VALUES (?,?,?,?,?)',r_id,b_id,u_id,rating,review_text)
    print("Review inserted")