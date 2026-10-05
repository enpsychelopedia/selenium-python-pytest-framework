


import pymysql
from seleframework.helpers.config_helpers import get_database_credentials
from seleframework.configs.generic_configs import GenericConfigs

def execute_from_db(sql):

    db_creds = get_database_credentials()

    connect = pymysql.connect(
        host = db_creds["host"],
        port = db_creds["port"],
        user = db_creds["user"],
        password = db_creds["password"]
    )

    try: 
        cursor = connect.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally: 
        connect.close()

    return db_data

def get_order_no_from_db(order_no):

    schema = GenericConfigs.SCHEMA
    table_prefix = GenericConfigs.TABLE_PREFIX

    sql = f'SELECT * FROM {schema}.{table_prefix}wc_orders WHERE id = {order_no};'

    db_order = execute_from_db(sql)

    return db_order