import pymongo

db = pymongo.MongoClient('mongodb://localhost:27017')
link_base = db['superurl']['linkBase']


def pushToDatabase(link_code: str, original_link: str):
    input_schema = {
        '_id': link_code,
        'original_link': original_link
    }

    link_base.insert_one(input_schema)


def searchInDatabase(link_code: str):
    url = link_base.find_one({"_id": link_code})
    if url:
        return True
    else:
        return False


def getLink(link_code: str):
    url = link_base.find_one({"_id": link_code})
    return url['original_link']


if __name__ == "__main__":
    
    pass
