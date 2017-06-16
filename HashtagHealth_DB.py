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

def delete_table(conn, delete_table_sql):
    """ delete a table from the delete_table_sql statement
    :param conn: Connection object
    :param delete_table_sql: a DROP TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(delete_table_sql)
    except exceptions as e:
        print(e)

def main():
    database = "C:\\sqlite\db\pythonsqlite.db"

    sql_create_main_table = """ CREATE TABLE IF NOT EXISTS main (
                                        id INTEGER PRIMARY KEY,
                                        Tweet_ID INT NOT NULL,
                                        Location INT NOT NULL,
                                        DateTime INT NOT NULL,
                                        Profile_location INT,
                                        Full_Tweet VARCHAR(400) NOT NULL,
                                        Hashtags TEXT,
                                        Mentions TEXT,
                                        BuzzWords TEXT
                                    ); """

    sql_create_region_table = """ CREATE TABLE IF NOT EXISTS region (
                                        id INTEGER PRIMARY KEY,
                                        Locale INT NOT NULL,
                                        Country VARCHAR(25),
                                        State VARCHAR (10),
                                        City VARCHAR(25)
                                        ); """

    sql_create_tweets_table = """ CREATE TABLE IF NOT EXISTS tweets (
                                        id INTEGER PRIMARY KEY,
                                        Tweet_ID INT NOT NULL,
                                        Tweet_Text TEXT NOT NULL,
                                        Topic VARCHAR(25),
                                        DateTime TEXT NOT NULL,
                                        Bio_Location VARCHAR(25),
                                        Tweet_Location VARCHAR(25)
                                        ); """

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY,
                                        User_ID VARCHAR(25),
                                        Twitter_Handle VARCHAR(25),
                                        Region VARCHAR(25)
                                        ); """

    sql_create_tweeted_by_table = """ CREATE TABLE IF NOT EXISTS tweeted_by (
                                        id INTEGER PRIMARY KEY,
                                        User_ID VARCHAR(25),
                                        Tweet_ID INT NOT NULL
                                        ); """

    sql_create_trends_table = """ CREATE TABLE IF NOT EXISTS trends (
                                        id INTEGER PRIMARY KEY,
                                        Trend_Topic VARCHAR(25),
                                        DateTime INT NOT NULL,
                                        Region VARCHAR(25)
                                        ); """

    sql_create_categories_table = """ CREATE TABLE IF NOT EXISTS categories (
                                        id INTEGER PRIMARY KEY,
                                        Category VARCHAR(25)
                                        ); """

    sql_create_buzzwords_table = """ CREATE TABLE IF NOT EXISTS buzzwords (
                                        id INTEGER PRIMARY KEY,
                                        Buzzword VARCHAR(25)
                                        ); """

    sql_create_topics_table = """ CREATE TABLE IF NOT EXISTS topics (
                                        id INTEGER PRIMARY KEY,
                                        Category VARCHAR(25),
                                        Buzzword VARCHAR(25)
                                        ); """

    sql_delete_topics = """ DROP TABLE IF EXISTS topics; """
    sql_delete_buzzwords = """ DROP TABLE IF EXISTS buzzwords; """
    sql_delete_categories = """ DROP TABLE IF EXISTS categories; """
    sql_delete_trends = """ DROP TABLE IF EXISTS trends; """
    sql_delete_tweeted_by = """ DROP TABLE IF EXISTS tweeted_by; """
    sql_delete_users = """ DROP TABLE IF EXISTS users; """
    sql_delete_tweets = """ DROP TABLE IF EXISTS tweets; """
    sql_delete_region = """ DROP TABLE IF EXISTS region; """
    sql_delete_main = """ DROP TABLE IF EXISTS main; """


    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # delete all tables first
        delete_table(conn, sql_delete_topics)
        delete_table(conn, sql_delete_buzzwords)
        delete_table(conn, sql_delete_categories)
        delete_table(conn, sql_delete_trends)
        delete_table(conn, sql_delete_tweeted_by)
        delete_table(conn, sql_delete_users)
        delete_table(conn, sql_delete_tweets)
        delete_table(conn, sql_delete_region)
        delete_table(conn, sql_delete_main)

        # create table
        create_table(conn, sql_create_main_table)
        create_table(conn, sql_create_region_table)
        create_table(conn, sql_create_tweets_table)
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_tweeted_by_table)
        create_table(conn, sql_create_trends_table)
        create_table(conn, sql_create_categories_table)
        create_table(conn, sql_create_buzzwords_table)
        create_table(conn, sql_create_topics_table)

    else:
        print("Error! cannot create the database connection.")



if __name__ == '__main__':
    main()