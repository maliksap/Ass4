import sqlite3


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO Suppliers (id,name,logistic) VALUES (?,?,?)
            """, [supplier.id, supplier.name, supplier.logistic])
        self._conn.commit()

