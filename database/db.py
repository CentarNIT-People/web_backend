import os
import certifi
from pymongo import MongoClient


def connect_to_db(collection_name: str):
    CONNECTION_STRING = os.environ["MONGODB_URL"]
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
    return client["data"][collection_name]