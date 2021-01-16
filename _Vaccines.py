import sqlite3


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn
        self._num_of_vaccines = 1

    def get_num_of_vaccines(self):
        return self._num_of_vaccines

    def insert(self, vaccine):
        self._conn.execute("""
                INSERT INTO Vaccines (id,date,supplier,quantity) VALUES (?,?,?,?)
            """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])
        self._conn.commit()
        self._num_of_vaccines = self._num_of_vaccines+1



