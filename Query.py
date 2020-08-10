import mysql.connector
import time
mydb = mysql.connector.connect(host='localhost', user='root',password='',database = 'ddm_dataset')
D_0 = mysql.connector.connect(host='localhost', user='root',password='',database = 'dataset_0')
D_1 = mysql.connector.connect(host='localhost', user='root',password='',database = 'dataset_1')
D_2 = mysql.connector.connect(host='localhost', user='root',password='',database = 'dataset_2')
D_3 = mysql.connector.connect(host='localhost', user='root',password='',database = 'dataset_3')
D_4 = mysql.connector.connect(host='localhost', user='root',password='',database = 'dataset_4')





#Get Min and Max likes from tables
s_0 = "select MIN(likes) from first"
s_1 = "select MAX(likes) from first"
cur1 = D_0.cursor()
cur1.execute(s_0)
min_0 = cur1.fetchone()[0]
cur1.execute(s_1)
max_0 = cur1.fetchone()[0]

print(min_0,max_0)

#Get Min and Max likes from tables
s_0 = "select MIN(likes) from second"
s_1 = "select MAX(likes) from second"
cur1 = D_1.cursor()
cur1.execute(s_0)
min_1 = cur1.fetchone()[0]
cur1.execute(s_1)
max_1 = cur1.fetchone()[0]

print(min_1,max_1)

#Get Min and Max likes from tables
s_0 = "select MIN(likes) from third"
s_1 = "select MAX(likes) from third"
cur1 = D_2.cursor()
cur1.execute(s_0)
min_2 = cur1.fetchone()[0]
cur1.execute(s_1)
max_2 = cur1.fetchone()[0]

print(min_2,max_2)

#Get Min and Max likes from tables
s_0 = "select MIN(likes) from fourth"
s_1 = "select MAX(likes) from fourth"
cur1 = D_3.cursor()
cur1.execute(s_0)
min_3 = cur1.fetchone()[0]
cur1.execute(s_1)
max_3 = cur1.fetchone()[0]


print(min_3,max_3)

#Get Min and Max likes from tables
s_0 = "select MIN(likes) from fifth"
s_1 = "select MAX(likes) from fifth"
cur1 = D_4.cursor()
cur1.execute(s_0)
min_4 = cur1.fetchone()[0]
cur1.execute(s_1)
max_4 = cur1.fetchone()[0]

print(min_4,max_4)
	



#Two Variables
min_limit = 10000
max_limit = 100000


D_00 = False
D_10 = False
D_20 = False
D_30 = False
D_40 = False

if min_limit < max_0 and max_limit > min_0:
	D_00 = True

if min_limit < max_1 and max_limit > min_1:
	D_10 = True	

if min_limit < max_2 and max_limit > min_2:
	D_20 = True	

if min_limit < max_3 and max_limit > min_3:
	D_30 = True	

if min_limit < max_4 and max_limit > min_4:
	D_40 = True			

print("DataBases: ",D_00 , D_10 , D_20 , D_30 , D_40)



start = time.time()

count = 0
if D_00 == True:
	s_0 = "select * from first where likes >= %s AND likes <= %s"
	cur_0 = D_0.cursor()
	T = (min_limit , max_limit)
	cur_0.execute(s_0,T)
	result = cur_0.fetchall()
	for res in result:
		count = count + 1

if D_10 == True:
	s_0 = "select * from second where likes >= %s AND likes <= %s"
	cur_0 = D_1.cursor()
	T = (min_limit , max_limit)
	cur_0.execute(s_0,T)
	result = cur_0.fetchall()
	for res in result:
		count = count + 1
		

if D_20 == True:
	s_0 = "select * from third where likes >= %s AND likes <= %s"
	cur_0 = D_2.cursor()
	T = (min_limit , max_limit)
	cur_0.execute(s_0,T)

	result = cur_0.fetchall()
	for res in result:
		count = count + 1

if D_30 == True:
	s_0 = "select * from fourth where likes >= %s AND likes <= %s"
	cur_0 = D_3.cursor()
	T = (min_limit , max_limit)
	cur_0.execute(s_0,T)
	result = cur_0.fetchall()
	for res in result:
		count = count + 1

if D_40 == True:
	s_0 = "select * from fifth where likes >= %s AND likes <= %s"
	cur_0 = D_4.cursor()
	T = (min_limit , max_limit)
	cur_0.execute(s_0,T)
	result = cur_0.fetchall()
	for res in result:
		count = count + 1

finish = time.time()

print(count , " rows affected in the range: ",min_limit," ",max_limit)
print("Query took ",finish-start, " seconds")