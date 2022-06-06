from quicksqlconnector import quicksqlconnector

db = quicksqlconnector('localhost', 6606,'root', 'anas9916', 'superurl')

db.query('create database if not exists superurl')
db.query('use superurl')
db.query('create table if not exists linkBase(id varchar(10) primary key, originalLink varchar(1000))')

def pushToDatabase(link_code: str, original_link: str):
    db.query(f'insert into linkBase values("{link_code}","{original_link}")')

def searchInDatabase(link_code: str):
    url = db.query(f'select originalLink from linkBase where id="{link_code}"')
    if url : return True
    else :return False


def getLink(link_code: str):
    return db.query(f'select originalLink from linkBase where id="{link_code}"')[0][0]

if __name__ == "__main__":
    pass