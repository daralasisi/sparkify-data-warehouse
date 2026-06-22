"""
This script creates the Redshift database tables for the Sparkify Data Warehouse project and completes the following:
1. Connects to Amazon Redshift.
2. Drops existing tables if they exist.
3. Creates staging, fact, and dimension tables.
"""

import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    This function drops all staging and analytics tables if they already exist.

    Args:
        cur: Database cursor.
        conn: Database connection.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    This function creates all staging and analytics tables.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Establish a Redshift connection and execute the table creation process.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()