__author__ = 'Anubhav'



import mysql.connector


dbo = mysql.connector

print "opening db connection"

cnx = dbo.connect(user='mysqluser',password='anupallavi19',host='127.0.0.1',database='shypz')

cursor = cnx.cursor()

sql = "select * from user_info"



try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   rows = len(results)
   print rows
   for row in results:
      id = row[0]
      name = row[1]
      place = row[2]
      m1 = row[3]
      m2 = row[4]
      m3 = row[5]
      # Now print fetched result
      print "id=%d,name=%s,place=%s,marks1=%d,marks2=%d,marks3=%d" % \
             ( id,name,place,m1,m2,m3)


except:
   print "Error: unable to fecth data"


cnx.close()


print "db connection closed"

