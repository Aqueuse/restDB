import json

from pymongo import MongoClient

client = MongoClient('localhost', 27017)


def is_database_exist(database_name):
    databases = client.list_database_names()
    for database in databases:
        if database == database_name:
            return True
    return False


def find_one_in_collection(database_name, collection_name, mongo_filter):
    if not is_database_exist(database_name):
        return "database dont exist"
    else:
        collection = client.get_database(database_name)[collection_name]
        element = collection.find_one(json.loads(mongo_filter))
        return element


def find_all_in_collection(database_name, collection_name, mongo_filter):
    if not is_database_exist(database_name):
        return "database dont exist"
    else:
        collection = client.get_database(database_name).get_collection(collection_name)
        element = collection.find(json.loads(mongo_filter))
        return element


def append_to_collection(database_name, collection_name, collection_element):
    if not is_database_exist(database_name):
        return "database dont exist"
    else:
        collection = client.get_database(database_name).get_collection(collection_name)
        element_id = collection.insert_one(json.loads(collection_element))
        return element_id


def update_item_in_collection(database_name, collection_name, mongo_filter, mongo_values):
    if not is_database_exist(database_name):
        return "database dont exist"
    else:
        collection = client.get_database(database_name).get_collection(collection_name)
        element_id = collection.update_one(json.loads(mongo_filter), json.loads(mongo_values))
        return element_id.raw_result


def delete_item_in_collection(database_name, collection_name, mongo_filter):
    if not is_database_exist(database_name):
        return "database dont exist"
    else:
        collection = client.get_database(database_name).get_collection(collection_name)
        element_id = collection.delete_one(json.loads(mongo_filter))
        return element_id.raw_result
