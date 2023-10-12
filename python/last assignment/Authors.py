from dbutils import result_as_dict
def get_all_authors(cursor):
    cursor.execute('select * from Authors')
    results=result_as_dict(cursor)
    for result in results:
        print(result)

def remove_author(cursor,id):
    cursor.execute('DELETE from Authors where authorid=?',id)
    print(f'{id} Deleted')

def add_author(cursor,id,name,bio):
    cursor.execute('insert into Authors (authorid,name,bio) VALUES (?,?,?)',id,name,bio)
    print(f'{id} added')

def author_by_id(cursor,id):
    cursor.execute('select * from Authors where authorid=?',id)
    results= result_as_dict(cursor)
    for res in results:
            print(res)

def update_author(cursor,id,name=None,bio=None):
    if name != None and bio!=None:
        cursor.execute('UPDATE Authors SET name=?,bio=? WHERE authorid=?',name,bio,id)
        print(f'{id} is updated with name {name} and bio {bio}')
    elif name==None and bio!=None:
        cursor.execute('UPDATE Authors SET bio=? WHERE authorid=?',bio,id)
        print(f'{id} is updated with bio {bio}')
    elif bio==None and name!=None:
        cursor.execute('UPDATE Authors SET name=? WHERE authorid=?',name,id)
        print(f'{id} is updated with name {name} ')

def get_author_review(cursor,id):
    cursor.execute('''SELECT B.title, R.rating, R.review_text 
                      FROM Reviews R
                      JOIN Books B ON R.bookid = B.bookid
                      WHERE B.authorid = ?''',id)
    results=result_as_dict(cursor)
    for res in results:
            print(res)


    