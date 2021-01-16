import sqlite3


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
                INSERT INTO Clinics (id,location,demand,logistic) VALUES (?,?,?,?)
            """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])
        self._conn.commit()

