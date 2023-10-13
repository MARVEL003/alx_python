# imported these packages for use
import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # created a variable that establishes connection to MySQL server
    database = MySQLdb.connect(host="localhost", port=3306,
                               user=username,
                               passwd=password,
                               db=database)

    cursor = database.cursor()
    query = "SELECT id, name FROM states \
            WHERE BINARY name =%s \
            ORDER BY id ASC"

    state_name = sys.argv[4]

    # executing a query with the provided state_name
    cursor.execute(query, (state_name, ))

    # fetch all the matching rows
    states = cursor.fetchall()

    for state in states:
        print(state)

    # close both cursor and database connection
    cursor.close()
    database.close()