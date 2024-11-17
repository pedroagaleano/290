import pymysql

db_host = "database-1.cb02msws2kc0.us-east-1.rds.amazonaws.com"
db_user = "peter"
db_passw = "Sacada#77"

try:
    connection = pymysql.connect(
        host = db_host,
        user = db_user,
        password = db_passw
    )
    print("succefull connection to DB")
except Exception as err:
    print("Error:", err)
    connection = None

def add_user(id, name, lastname, birthday):
    instruction_sql = "INSERT INTO db_usr.usrs(id, name, lastname, birthday) VALUES ("+id+", '"+name+"', '"+lastname+"','"+birthday+"')"
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        connection.commit()
        print("user add")
    except Exception as err:
        print("Error:", err)

def consult_user(id):
    instruction_sql = "SELECT * FROM db_usr.usrs WHERE id="+id 
    try:
        cursor = connection.cursor()
        cursor.execute(instruction_sql)
        result = cursor.fetchall()
        print("User consulted")
        return result
    except Exception as err:
        print("Error:", err)
