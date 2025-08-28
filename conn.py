import psycopg2 as pgsql_dbengine

#Initialize database connection
conn = pgsql_dbengine.connect(database="studportal", user="postgres",
                        password="root", host="localhost", port="5432")