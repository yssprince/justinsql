import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Justin1959',
)

print("Connected to MySQL!")

import mysql.connector

def fetch_name_birth_month():
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Justin1959',
            database='menagerie'  # Specify your database name
        )

        if connection.is_connected():
            # Create cursor to interact with the database
            cursor = connection.cursor()

            # Query to select 'name', 'birth', and extract birth month from the 'pet' table
            select_query = '''
            SELECT name, birth, MONTH(birth) AS birth_month
            FROM pet
            '''

            # Execute the query
            cursor.execute(select_query)

            # Fetch all records
            records = cursor.fetchall()

            # Display fetched records
            if len(records) > 0:
                print("Name, Birth, and Birth Month:")
                for record in records:
                    print(f"Name: {record[0]}, Birth: {record[1]}, Birth Month: {record[2]}")
            else:
                print("No records found.")

            # Close the cursor
            cursor.close()

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Close the connection
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

# Call the function to fetch 'name', 'birth', and 'birth month' columns from the 'pet' table
fetch_name_birth_month()
