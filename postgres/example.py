import psycopg2

# Define your database connection parameters
db_params = {
    'dbname': 'pagila',
    'user': 'ricardovieira',
    'password': 'test123.',
    'host': '127.0.0.1',  # Typically 'localhost' or '127.0.0.1' for a local database
    'port': '5432'  # Default PostgreSQL port is 5432
}

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
    exit()

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Execute a SQL query to fetch data
query = "select i1 from t1;"
try:
    cursor.execute(query)
except psycopg2.Error as e:
    print("Error executing the query:", e)
    connection.close()
    exit()

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and the database connection
cursor.close()
connection.close()
