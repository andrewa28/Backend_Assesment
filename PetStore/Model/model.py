'''
A file to handle database and its functions
'''
import sqlite3
from flask import g
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "PetStore.db")

# DATABASE = 'PetStore.db'
DATABASE = os.path.join(BASE_DIR, "PetStore.db")


# calling the database
def get_database():
    database = sqlite3.connect(DATABASE, check_same_thread=False)
    database.row_factory = sqlite3.Row
    return database


# closing the database, important step to save the changes
def close_database():
    database = g.pop('db', None)
    if database is not None:
        database.close()


def insert_bid(pet_id, user_id, amount):
    database = get_database()
    database_cursor = database.cursor()
    database_cursor.execute("PRAGMA foreign_keys=ON;")

    database_cursor.execute('insert into Bid (pet_id,user_id,amount) values (?,?,?)', (pet_id, user_id, amount))

    database.commit()
    database.close()


# return all the bids in the database
def get_allBids():
    database = get_database()
# Database query
    rows = database.cursor().execute('SELECT User.username,Pet.name,Bid.amount,Category.category_name '
                                     'FROM User '
                                     'JOIN Bid '
                                     'ON User.id = Bid.user_id '
                                     'JOIN Pet '
                                     'ON Pet.id = Bid.pet_id '
                                     'JOIN Category '
                                     'ON Pet.category_id = Category.id')
#     rows = database.cursor().execute('SELECT * FROM Bid')

# To return them in the look of a dictionary (json files' look)
    returned_rows = []
    for row in rows:
        bidDictionary = {
            'pet_name': row['name'],
            'Category': row ['category_name'],
            'user_name': row['username'],
            'amount': row['amount']
        }
        returned_rows.append(bidDictionary)
    database.close()
    return returned_rows


# database query to return the bids on a specific pet
def get_specificPetBids(specificPet_id):
    database = get_database()
    # Database query
    rows = database.cursor().execute('SELECT User.username,Pet.name,Bid.amount,Category.category_name '
                                     'FROM User '
                                     'JOIN Bid '
                                     'ON User.id = Bid.user_id '
                                     'JOIN Pet '
                                     'ON Pet.id = Bid.pet_id '
                                     'JOIN Category '
                                     'ON Pet.category_id = Category.id '
                                     'WHERE '+str(specificPet_id)+' =Bid.pet_id')

    # To return them in the look of a dictionary (json files' look)
    returned_rows = []
    for row in rows:
        bidDictionary = {
            'Pet_name': row['name'],
            'Category': row['category_name'],
            'Bidder': row['username'],
            'Amount': row['amount']
        }
        returned_rows.append(bidDictionary)
    database.close()
    return returned_rows

# print(get_allBids())
# print(insert_bid(3,1,100))
# print(get_allBids())
# print(get_specificPetBids(1))