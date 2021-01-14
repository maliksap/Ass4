import sqlite3


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
                INSERT INTO Clinics (id,location,demand,logistic) VALUES (?,?,?,?)
            """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])
        self._conn.commit()

    # def print_table(self):
    #     cur =self._conn.cursor()
    #     cur.execute("""SELECT Employees.id ,Employees.name, Employees.salary, Employees.coffee_stand FROM Employees
    #                 ORDER BY id ASC
    #                 """)
    #     print("Employees")
    #     for row in cur.fetchall():
    #         print(row)
    #
    # def print_report(self):
    #     cur = self._conn.cursor()
    #     cur.execute("""SELECT Employees.name,Employees.salary, Coffee_stands.location, ifnull(SUM(Activities.quantity*Products.price*(-1)),0) AS sales FROM Employees
    #     LEFT JOIN Activities
    #     ON Employees.id=Activities.activator_id
    #     LEFT JOIN Products
    #     ON Activities.product_id=Products.id
    #     LEFT JOIN Coffee_stands ON Employees.coffee_stand=Coffee_stands.id
    #     GROUP BY Employees.id
    #     ORDER BY Employees.name ASC;
    #     """)
        #
        # print("Employees report")
        # for row in cur.fetchall():
        #     to_print=""
        #     for item in row:
        #         to_print=to_print+str(item)+" "
        #     print(to_print)