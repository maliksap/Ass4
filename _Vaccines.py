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
    #     #
    #     print("Employees report")
    #     for row in cur.fetchall():
    #         to_print=""
    #         for item in row:
    #             to_print=to_print+str(item)+" "
    #         print(to_print)
