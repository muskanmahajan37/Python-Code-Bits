import mysql.connector
con = mysql.connector.connect(user='root', password = 'tigermanudon!1234' ,host='127.0.0.1')
mycursor=con.cursor()
#mycursor.execute("Create database engineer")
mycursor.execute(" use engineer")
mycursor.execute(""" create table tb1(id int primary key,
#name varchar(30),
#salary int,
#city varchar(30))""")
mycursor.execute("insert into tb2 values(1,'muskaan',750000,'australia')")
con.commit()
print("created")
#mycursor.execute("insert into tb2 values(2,'ram', '65000','london')")
#con.commit()
#print("created")
#mycursor.execute("insert into tb1 values(3,'jasmine',850000,'delhi')")
#con.commit()
#print("created")
#mycursor.execute(insert into tb1 values(4,'harpreet',55000,'america')")
#con.commit()
#print("created")
