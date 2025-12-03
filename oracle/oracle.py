import cx_Oracle

# Replace these values with your Oracle database connection details
db_user = "ricardo"
db_password = "Test123_"
db_dsn = "127.0.0.1:1521/test01"

# Establish a connection to the Oracle database
connection = cx_Oracle.connect(user=db_user, password=db_password, dsn=db_dsn)

# Create a cursor
cursor = connection.cursor()

try:
    # Execute a sample query
    cursor.execute("SELECT * FROM t1")

    # Fetch and print the results
    for row in cursor:
        print(row)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()