import exceptions
import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except exceptions as e:
        print(e)

    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except exceptions as e:
        print(e)


def main():
    database = "C:\\sqlite\db\pythonsqlite.db"

    sql_create_main_table = """ CREATE TABLE IF NOT EXISTS main (
                                        id INTEGER PRIMARY KEY,
                                        Location INT NOT NULL,
                                        Time INT NOT NULL,
                                        Profile_location INT,
                                        Full_Tweet VARCHAR(400) NOT NULL,
                                        Hashtags TEXT,
                                        Mentions TEXT,
                                        BuzzWords TEXT
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create table
        create_table(conn, sql_create_main_table)
    else:
        print("Error! cannot create the database connection.")



if __name__ == '__main__':
    main()