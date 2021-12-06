import psycopg2

def createtables():
    conn = psycopg2.connect(database = "db1", user="postgres", 
                            password="password")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS data
        (
        id int primary key,
        name char(20),
        roll INTEGER,
        mark REAL
        )""")
    conn.commit()
    conn.close()

createtables()

def insert(id,name,roll,mark):
    conn = psycopg2.connect(database = "db1", user="postgres",password="password")
    cur = conn.cursor()

    cur.execute("""INSERT INTO data VALUES('%s','%s','%s','%s')"""%\
                (id,name,roll,mark))


    conn.commit()
    conn.close()

# insert(3,"puggy",6,100)


def view():
    conn = psycopg2.connect(database = "db1", user="postgres",password="password")
    cur = conn.cursor()

    cur.execute("SELECT * FROM data")
    v = cur.fetchall()
    conn.commit()
    conn.close()
    return v

print(view())

def delete(f):
    conn = psycopg2.connect(database = "db1", user="postgres",password="password")
    cur = conn.cursor()

    cur.execute("DELETE FROM data WHERE id = %s" , (f,))

    conn.commit()
    conn.close()

delete(3)
print(view())

def update(name,id):
    conn = psycopg2.connect(database = "db1", user="postgres",password="password")
    cur = conn.cursor()

    cur.execute("UPDATE data SET name = %s WHERE id = %s", (name,id))

    conn.commit()
    conn.close()
update('newwer',2)
print(view())
    
