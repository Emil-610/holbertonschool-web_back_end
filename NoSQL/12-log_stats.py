#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Print the number of logs, the count per HTTP method and the number
    of status check requests in the given collection."""
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_count))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_stats(client.logs.nginx)
