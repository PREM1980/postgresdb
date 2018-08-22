"""PostgresDbContext module"""
import os
import time
import psycopg2.extras
import sys
from log import LOGGER


class PgDbContext(object):
    """ This module is used to interface with postgres database"""

    @staticmethod
    def build_from_environment():
        """ static utility method that creates a connection object"""

        pg_username = os.environ['POSTGRES_USERNAME']
        pg_password = os.environ['POSTGRES_PASSWORD']

        try:
            conn = psycopg2.connect("user=" + pg_username + " host='localhost' password=" + pg_password)
        # program ends if the connection fails.
        except psycopg2.OperationalError, oe:
            raise oe
            sys.exit(1)

        return PgDbContext(conn)

    def __init__(self, conn,
                 max_retries=3,
                 retry_period=5):
        self.conn = conn
        self._max_retries = max_retries
        self._retry_period = retry_period

    def get_cursor(self):
        """ returns a cursor for the connection"""
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def execute(self, qry):
        """ returns a function that executes the query and returns the result"""
        def internal():
            print 'qry = ', qry
            self._cur = self.get_cursor()
            print 'self._cur = ', self._cur
            self._cur.execute(qry)
            # self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor).execute(qry)
            rows = self._cur.fetchall()
            return rows

        return self._retry(internal)

    def _retry(self, f):
        """ The query is executed multiple times to overcome any operational
            error. Database error is logged immediately."""
        count = 0
        while True:
            try:
                return f()
            # http://initd.org/psycopg/docs/module.html#psycopg2.DatabaseError
            # handle operational error - memory allocation, unexpected disconnect
            except psycopg2.OperationalError, oe:
                count += 1
                if count < self._max_retries:
                    LOGGER.warn("Transient Error Received %s ", oe)
                    time.sleep(self._retry_period)
                else:
                    LOGGER.error("Unrecoverable Error %s", oe)
                    raise oe
            # other database errors - integrity, internal, programming error etc
            except psycopg2.DatabaseError, de:
                LOGGER.error("Database Error %s", de)
                raise de
            # interface errors
            except psycopg2.Error, e:
                raise e

    def close(self):
        """ closes the connection"""
        self._conn.close()
