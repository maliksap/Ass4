import sqlite3


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""
                INSERT INTO Logistics (id,name,count_sent,count_received) VALUES (?,?,?,?)
            """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])
        self._conn.commit()

