import json
from pymongo import MongoClient

port_number = int(input('Server port number: '))    # prompt asking for port number

client = MongoClient("localhost", port_number)      # connect to server

db = client['291db']    # open database

name_basics = db['name_basics']     # open or create collections
title_basics = db['title_basics']
title_principals = db['title_principals']
title_ratings = db['title_ratings']

def drop_collections():
    """
        Drop previous collections.

        Argument: None

        Returns: None
    """
    name_basics.drop()
    title_basics.drop()
    title_principals.drop()
    title_ratings.drop()

    return


def create_collections():
    """
        Create collections after dropping previous ones.

        Arguments: None

        Returns: None
    """
    drop_collections()

    json2mongo('name.basics.json', name_basics)
    json2mongo('title.basics.json', title_basics)
    json2mongo('title.principals.json', title_principals)
    json2mongo('title.ratings.json', title_ratings)

    return


def json2mongo(input_file, collection):
    """
        Insert into collections.

        Arguments:
            input_file: path to json file
            collection: collection name

        Returns: None
    """
    with open(input_file, 'r', encoding='utf-8') as f:    # open json file

        data = json.load(f)     # load data from json file

        collection.insert_many(data)    # insert data into the collection

    return


def main():
    create_collections()

    return

if __name__ == "__main__":
    main()
