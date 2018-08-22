
# # import psycopg2
# import psycopg2.extras
#
# try:
#     conn = psycopg2.connect("user='postgres' host='localhost' password='postgres'",
#                             )
# except:
#     print "I am unable to connect to the database"
#
# cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#
# cur.execute("""SELECT datname from pg_database""")
#
#
# rows = cur.fetchall()
# print "\nShow me the databases:\n"
# print rows
# print "   ", row[0]
# for row in rows:
#     print row

import os
import psycopg2
print 'hello'
from tests.postgresdb.pgconn import PgDbContext


os.environ["POSTGRES_USERNAME"] = 'postgres'
os.environ["POSTGRES_PASSWORD"] = 'postgres'

x = PgDbContext.build_from_environment()
for each in x.execute("""SELECT datname from pg_database"""):
    print each

# print 'hello'
