
"""
Runs the ETL pipeline for the Sparkify Data Warehouse project by completing the following:
1. Loads raw JSON data from S3 into Redshift staging tables.
2. Transforms the staged data.
3. Inserts data into fact and dimension tables.
"""

import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    This function executes COPY commands to load data from S3 into staging tables.
    """
    for i, query in enumerate(copy_table_queries, start=1):
        print(f"Running COPY query {i}...")
        cur.execute(query)
        conn.commit()
        print(f"COPY query {i} completed")


def insert_tables(cur, conn):
    """
    This function inserts transformed data from staging tables into fact and dimension tables.
    """
    for i, query in enumerate(insert_table_queries, start=1):
        print(f"Running INSERT query {i}...")
        cur.execute(query)
        conn.commit()
        print(f"INSERT query {i} completed")


def main():
     """
    This function establishes a Redshift connection and execute the ETL pipeline.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()