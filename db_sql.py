from quicksqlconnector import quicksqlconnector

db = quicksqlconnector('localhost', 6606,'root', 'anas9916', 'superurl')

db.query('create database if not exists superurl')
db.query('use superurl')
db.query('create table if not exists linkBase(id varchar(100) primary key, passCode varchar(50), originalLink varchar(2000))')
db.query('create table if not exists problemReported(msg varchar(500) primary key)')

def pushToDatabase(link_code: str, passcode : str, original_link: str):
    db.query(f'insert into linkBase values("{link_code}","{passcode}","{original_link}")')

def searchInDatabase(link_code: str):
    url = db.query(f'select originalLink from linkBase where id="{link_code}"')
    if url : return True
    else : return False

def getLink(link_code: str):
    return db.query(f'select originalLink from linkBase where id="{link_code}"')[0][0]

def checkPass(link_code: str):
    password = db.query(f'select passCode from linkBase where id="{link_code}"')[0][0]
    if password : return True
    else : return False

def matchPassword(link_code: str, passcode : str):
    password = db.query(f'select passCode from linkBase where id="{link_code}"')[0][0]
    if passcode == password:
        return True
    return False

def availableHandle(custom_handle : str):
    print(custom_handle)
    custom_handle_found = db.query(f'select id from linkBase where id="{custom_handle}"')
    if custom_handle_found : return True
    else : return False
# -----------------------------------
def submitProblem(problem_statement : str):
    db.query(f'insert into problemReported values("{problem_statement}")')

if __name__ == "__main__":
    # print(availableHandle('mylovelysite'))
    pass