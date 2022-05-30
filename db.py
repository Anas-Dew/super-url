import pymongo

db = pymongo.MongoClient('mongodb://public_user:me0IUpVVaY1PmvWV@copywordbase-shard-00-00.pya1y.mongodb.net:27017,copywordbase-shard-00-01.pya1y.mongodb.net:27017,copywordbase-shard-00-02.pya1y.mongodb.net:27017/test?replicaSet=atlas-dlvpl1-shard-0&ssl=true&authSource=admin')
link_base = db['urlShortner']['linkBase']


def pushToDatabase(link_code: str, original_link: str):
    input_style = {
        '_id': link_code,
        'original_link': original_link
    }

    link_base.insert_one(input_style)


def searchInDatabase(link_code: str):
    url = link_base.find_one({"_id": link_code})
    if url:
        return True
    else:
        return False


def getLink(link_code: str):
    url = link_base.find_one({"_id": link_code})
    return url['original_link']


# if __name__ == "__main__":
#     # print(searchInDatabase('0b67Gq'))
#     pass
