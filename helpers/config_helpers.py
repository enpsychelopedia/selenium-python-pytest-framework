


import os

def get_base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return  'http://localhost:8888/testsite/'
    elif env.lower() == 'prod':
        return  'http://localhost:8888/prod.testsite/'

def get_database_credentials():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        db_host = '127.0.0.1'
        db_port = 8889
    elif env.lower() == 'prod':
        db_host = 'localhost'
        db_port = 3001
    else: 
        raise Exception("Environment unknown.")

    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    if not db_user or not db_password:
        raise Exception("Environment variables: 'DB_USER' & 'DB_PASSWORD' must be set.")

    db_creds = {
        "host" : db_host,
        "port" : db_port,
        "user" : db_user,
        "password" : db_password
    }

    return db_creds