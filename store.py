from pymongo import MongoClient
import uuid
from datetime import datetime


def store_in_mongodb(trending_topics, ip_address):
    client = MongoClient("mongodb://localhost:27017")
    db = client['twitter_trends']
    collection = db['trends']

    data = {
        "_id": str(uuid.uuid4()),
        "trend1": trending_topics[0],
        "trend2": trending_topics[1],
        "trend3": trending_topics[2],
        "trend4": trending_topics[3],
        "trend5": trending_topics[4],
        "datetime": datetime.now(),
        "ip_address": ip_address
    }

    collection.insert_one(data)


# Example usage:
store_in_mongodb(trending_topics, "123.456.789.012")
