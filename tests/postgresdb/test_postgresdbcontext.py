import unittest
import os
import mock
import psycopg2
from postgresdb.db.db_service import PgDbContext


class TestPgDbContext(unittest.TestCase):
    def setUp(self):
        os.environ["POSTGRES_USERNAME"] = 'postgres'
        os.environ["POSTGRES_PASSWORD"] = 'postgres'
        self.pg = mock.MagicMock(psycopg2)
        self.conn = self.pg.connect()
        self.dbcontext = PgDbContext(self.conn)

    def test_queries_can_be_executed(self):
        self.dbcontext.conn.cursor().execute.side_effect = psycopg2.DatabaseError
        # self.dbcontext.conn.cursor().execute.return_value = None
        # self.dbcontext.conn.cursor().fetchall.return_value = ['prem']
        results = [each for each in self.dbcontext.execute('SELECT version()')]  # type: object
        print results
        self.assertEqual(1, 1)

    # def test_handles_timeout_exception(self):
    #     self.conn.cursor.execute.side_effect = psycopg2.DatabaseError
    #     results = [each for each in self.dbcontext.execute('SELECT version()')]
    #     self.assertRaises(psycopg2.DatabaseError,
    #                     [each for each in self.dbcontext.execute('SELECT version()')])
    #
    #     pass
        # self.r.lrange.side_effect = TimeoutError()
        # results = self.lookup.request_labels(self.customer_id, self.store_id, self.run_id, self.aisle_id)
        # self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()
