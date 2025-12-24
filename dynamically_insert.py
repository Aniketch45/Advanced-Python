import mysql.connector;                     

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

empid=int(input("Enter Employee id :"))
# ename=input("Enter Employee name :")
esal=int(input("Enter Employee Salary :"))

# query="insert into employee (eid,ename,esal) values (%s,%s,%s)"
query="update employee set esal=%s where eid=%s"
cur.execute(query,(esal,empid))
db.commit()
cur.close()
db.close()