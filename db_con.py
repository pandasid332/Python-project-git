import oracledb

def test_db_connection(username, password, dsn):
    """
    Test the connection to an Oracle database using oracledb library.

    :param username: Database username
    :param password: Database password
    :param dsn: Data Source Name (hostname:port/service_name)
    :return: None
    """
    try:
        # Establish the connection
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        
        # If connection is successful, print the version of the database
        print("Connection successful.")
        print("Oracle Database version:", connection.version)
        
        # Close the connection
        connection.close()
    except oracledb.DatabaseError as e:
        print("There was a problem connecting to the database:", e)

# Example usage
username = 'scott'
password = 'tiger'
dsn = 'localhost:1521/orclpdb'

test_db_connection(username, password, dsn)