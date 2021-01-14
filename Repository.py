# The Repository
import atexit
import sqlite3

from _Clinics import _Clinics
from _Logistics import _Logistics
from _Suppliers import _Suppliers
from _Vaccines import _Vaccines


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database3.db')
        self.vaccines = _Vaccines(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.clinics = _Clinics(self._conn)
        self.logistics = _Logistics(self._conn)

    def get_conn(self):
        return self._conn

    def get_vaccines(self):
        return self.vaccines

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        cur = self._conn.cursor()

        cur.executescript("""
            CREATE TABLE vaccines (
                id      INTEGER     PRIMARY KEY,
                date        DATE        NOT NULL,
                supplier        INTEGER     NOT NULL,
                quantity        INTEGER     REFERENCES Supplier(id)
            );

            CREATE TABLE suppliers (
                id      INTEGER     PRIMARY KEY,
                name        STRING      NOT NULL,
                logistic        INTEGER     REFERENCES Logistic(id)
            );

            CREATE TABLE clinics (
                id      INTEGER     PRIMARY KEY,
                location        STRING      NOT NULL,
                demand      INTEGER     NOT NULL,
                logistic        INTEGER     REFERENCES Logistic(id)
            );
            
            CREATE TABLE logistics (
                id      INTEGER     PRIMARY KEY,
                name        STRING      NOT NULL,
                count_sent      INTEGER     NOT NULL,
                count_received      INTEGER     NOT NULL
            );
        """)
        self._conn.commit()


# the repository singleton
repo = _Repository()
atexit.register(repo._close)
