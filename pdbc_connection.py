import mysql.connector

db = mysql.connector.connect(user="root",
                             password='9766',
                             host='localhost',
                             port=3306,
                             database='instagram')

if(db.is_connected()):
    print("Connected")
else:
    print("Failed to connect")

cur=db.cursor()

# sql="use instagram"
# cur.execute(sql)
# sql2="create table Employee(eid int,ename varchar(20),esal int)"
# cur.execute(sql2)

# sql2="insert into employee (eid,ename,esal) values(101,'Aniket',34242),(103,'viki',49349)"
# cur.execute(sql2)

# query="update employee set esal=40000 where ename='viki'"
# cur.execute(query)
query="delete from employee where ename='Aniket'"
cur.execute(query)
db.commit()
print(cur.rowcount)
# cur.execute("show tables")

# for i in cur:
#     print(i)

cur.close()
db.close()