import pyodbc as db
import os
from dbutils import result_as_dict
from Users import *
from Authors import *
from Books import *
from Reviews import *



def main():
    command_functions = {}

    driver='{ODBC Driver 18 for SQL Server}'
    server=r'localhost\SQLEXPRESS'
    database='assign_fin_db'
    # user='SA'
    # password=os.environ.get('DB_PASSWORD','')
    encrypt='no'
    trusted_connection='yes'

    connection_string=f'''
        DRIVER={driver};
        SERVER={server};
        DATABASE={database};
        trusted_connection={trusted_connection};
        ENCRYPT={encrypt};
    '''

    with db.connect(connection_string) as connection:
        print('connection successful')
    
        cursor= connection.cursor()
        command_functions["add_authors"] = add_author
        command_functions["remove_authors"] = remove_author
        command_functions["get_author_by_id"] = author_by_id
        command_functions["get_all_authors"] = get_all_authors
        command_functions["update_authors"] = update_author
        command_functions["get_author_reviews"] = get_author_review
        command_functions["add_books"] = add_book
        command_functions["add_book_review"] = add_book_review
        command_functions["remove_books"] = remove_book
        command_functions["get_all_books"] = get_all_books
        command_functions["get_book_by_authorid"] = get_books_by_authorid
        command_functions["get_book_reviews"] = get_book_review
        command_functions["add_book_review"] = add_book_review
        command_functions["get_all_review"] = get_all_reviews
        command_functions["add_user"] = add_new_user
        command_functions["get_all_user"] = get_all_users
        command_functions["get_user_review"] = get_user_review

        while True:
            user_input = input("db> ")
            parts = user_input.split(',')
            command = parts[0]
            arguments = parts[1:]

            try:
                if command.lower() in ["quit", "exit", "bye"]:
                    break
                command_functions[command.lower()](cursor,*arguments)
                
            except:
                print("Command not recognized.")

            
        




if __name__=='__main__':
    main()
