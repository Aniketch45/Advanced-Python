import mysql.connector;                        #post get put delete
                                               #Create read update delete

db=mysql.connector.connect(user='root',
                           password='9766',
                           host='localhost',
                           port=3306,                                                       
                           database='instagram')

if(db.is_connected()):
    print("connected")
else:
    print("not connected")

cur=db.cursor()

# sql2="insert into employee (eid,ename,esal) values(101,'Aniket',34242),(103,'viki',49349)"
# cur.execute(sql2)

query="select * from employee"
cur.execute(query)

# data=cur.fetchall()
# print(data)
# db.commit()
while True:
    data=cur.fetchone()
    if data==None:
        break
    print(data)
    

# for i in data:
#     print("id is",i[0],"name is",i[1],"salary is",i[2])

cur.close()
db.close()
