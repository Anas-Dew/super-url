from quicksqlconnector import quicksqlconnector

db = quicksqlconnector('mysql','localhost', 6606,'root', 'anas9916', 'superurl')

db.query('create database if not exists superurl')
db.query('use superurl')
db.query('create table if not exists linkBase(id varchar(100) primary key, passCode varchar(50), originalLink varchar(2000), ip_address varchar(30))')

def pushToDatabase(link_code: str, passcode : str, original_link: str, ip_address: str):
    db.query('insert into linkBase values(%s, %s, %s, %s)', (link_code, passcode, original_link, ip_address))

def searchInDatabase(link_code: str):
    url = db.query('select originalLink from linkBase where id=%s', (link_code,))
    if url : return True
    else : return False

def getLink(link_code: str):
    return db.query('select originalLink from linkBase where id=%s', (link_code,))[0][0]

def checkPass(link_code: str):
    password = db.query('select passCode from linkBase where id=%s', (link_code,))[0][0]
    if password : return True
    else : return False

def matchPassword(link_code: str, passcode : str):
    password = db.query('select passCode from linkBase where id=%s', (link_code,))[0][0]
    if passcode == password:
        return True
    return False

def availableHandle(custom_handle : str):
    custom_handle_found = db.query('select id from linkBase where id=%s', (custom_handle,))
    if custom_handle_found : return True
    else : return False
# -----------------------------------
def submitProblem(problem_statement : str):
    db.query('insert into problemReported values(%s)', (problem_statement,))

if __name__ == "__main__":
    # print(availableHandle('mylovelysite'))
    # print(submitProblem('it works'))
    pass