# listing out all tables in a certain database
import MySQLdb
import sys

# create a variable
database = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

# create a 'cursor', note it can be named anything
# using 'BINARY' before 'name' enables python know case-sensitive is needed
# N% is needed with BINARY for it to work
cursor = database.cursor()
cursor.execute(
    "SELECT id, name FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
database.close()