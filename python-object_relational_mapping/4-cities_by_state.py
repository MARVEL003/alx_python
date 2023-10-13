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

    # executing a query
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON state_id = states.id \
        ORDER BY cities.id ASC")

    # fetch all the matching rows
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    # close both cursor and database connection
    cursor.close()
    database.close()