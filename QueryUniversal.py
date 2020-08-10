import mysql.connector
import time
mydb = mysql.connector.connect(host='localhost', user='root',password='',database = 'ddm_dataset')

min_limit = 10000
max_limit = 100000
start = time.time()
count = 0
s_0 = "select * from mytable where likes >= %s AND likes <= %s"
cur_0 = mydb.cursor()	
T = (min_limit , max_limit)
cur_0.execute(s_0,T)
result = cur_0.fetchall()
for res in result:
	count = count + 1


finish = time.time()

print(count , " rows affected in the range: ",min_limit," ",max_limit)
print("Query took ",finish-start, " seconds")