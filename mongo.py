from ast import Str
from http import client
from pydoc import cli
from typing import Collection
from xmlrpc.client import DateTime
from dotenv import load_dotenv, find_dotenv
import urllib
import pprint
import os
from pymongo import MongoClient, mongo_client
from bson.objectid import ObjectId
import datetime



load_dotenv(find_dotenv())
password = urllib.parse.quote(os.environ.get("MONGO_PWD"))
print(password)
connection_srt = f"mongodb+srv://roshan0902:{password}@test-app.svle4.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(connection_srt)

db = client.voice_assistant
collection = db.remainder

def create_remainder():
    doc={
        "title": "This is a test title",
        "time": "27/2/2022"
    }
    collection.insert_one(doc)

create_remainder()