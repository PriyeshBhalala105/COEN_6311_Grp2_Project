import pymysql

conn = pymysql.connect(
    host = "database01.c5cpvw4flban.us-east-1.rds.amazonaws.com" ,
    user = "admin" ,
    password =  "BANNU2001200" ,
    port = 3306 
)

cur=conn.cursor()




