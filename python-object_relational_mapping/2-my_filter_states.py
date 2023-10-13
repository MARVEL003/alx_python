# imported these packages for use
import MySQLdb
import sys

# created a variable
database = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

cursor = database.cursor()
state_name = sys.argv[4]

cursor.execute(
    "SELECT id, name FROM states \
    WHERE BINARY name = '{}' \
    ORDER BY id ASC".format(state_name))
states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
database.close()