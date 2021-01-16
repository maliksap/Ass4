import sys
import sqlite3
import os
import Repository
from Clinic import Clinic
from Logistic import Logistic
# from Repository import _Repository
from Supplier import Supplier
from Vaccine import Vaccine

# def create_tables(conn):
#     cur = conn.cursor()
#
#     cur.execute("CREATE TABLE Employees (id INTEGER PRIMARY KEY,name TEXT NOT NULL,salary REAL NOT NULL,coffee_stand "
#                 "INTEGER REFERENCES Coffee_stand(id))")
#     cur.execute(" CREATE TABLE Suppliers (id INTEGER PRIMARY KEY,name TEXT NOT NULL,contact_information TEXT)")
#     cur.execute("CREATE TABLE Products(id INTEGER PRIMARY KEY,description TEXT NOT NULL,price REAL NOT NULL,"
#                 "quantity INTEGER NOT NULL)")
#     cur.execute("CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,location TEXT NOT NULL,number_of_employees INTEGER)")
#
#
# def insert_employee(employee, conn):
#     conn.execute("""
#             INSERT INTO Employees (id,name,salary,coffee_stand) VALUES (?,?,?,?)
#         """, [employee["id"], employee["name"], employee["salary"], employee["pos"]])
#
#
# def insert_supplier(supplier, conn):
#     conn.execute("""
#         INSERT INTO Suppliers(id,name,contact_information) VALUES(?,?,?)
#     """, [supplier["id"], supplier["name"], supplier["con_info"]])
#
#
# def insert_product(product, conn):
#     conn.execute("""
#         INSERT INTO Products (id,description,price,quantity) VALUES (?,?,?,?)
#     """, [product["id"], product["description"], product["price"], 0])
#
#
# def insert_coffee_stand(coff_stand, conn):
#     conn.execute("""
#         INSERT INTO Coffee_stands (id,location,number_of_employees) VALUES (?,?,?)
#     """, [coff_stand['id'], coff_stand['location'], coff_stand['num_of_employees']])
from order import order


def order_by_date(e):
    return e['id']


def initiate(args):
    # if os.path.isfile('database.db'):
    #     os.remove('database.db')
    repo = Repository.repo
    repo.create_tables()
    with open(args[1], 'r') as config_file:

        cnfg_list = config_file.read().splitlines()
        line_info = cnfg_list[0].split(",")
        num_of_vaccines = line_info[0]
        num_of_suppliers = line_info[1]
        num_of_clinics = line_info[2]
        num_of_logistics = line_info[3]
        vaccines_list = []
        for line in cnfg_list[1:int(num_of_vaccines) + 1]:
            line_splitted = line.split(",")
            id = line_splitted[0]
            date = line_splitted[1]
            supplier = line_splitted[2]
            quantity = line_splitted[3]
            repo.vaccines.insert(Vaccine(id, date, supplier, quantity))

        for line in cnfg_list[int(num_of_vaccines) + 1:int(num_of_vaccines) + int(num_of_suppliers) + 1]:
            line_splitted = line.split(",")
            id = line_splitted[0]
            name = line_splitted[1]
            logistic = line_splitted[2]
            repo.suppliers.insert(Supplier(id, name, logistic))

        for line in cnfg_list[int(num_of_vaccines) + int(num_of_suppliers) + 1:int(num_of_vaccines) + int(
                num_of_suppliers) + int(num_of_clinics) + 1]:
            line_splitted = line.split(",")
            id = line_splitted[0]
            location = line_splitted[1]
            demand = line_splitted[2]
            logistic = line_splitted[3]
            repo.clinics.insert(Clinic(id, location, demand, logistic))

        for line in cnfg_list[int(num_of_vaccines) + int(num_of_suppliers) + int(num_of_clinics) + 1:]:
            line_splitted = line.split(",")
            id = line_splitted[0]
            name = line_splitted[1]
            count_sent = line_splitted[2]
            count_received = line_splitted[3]
            repo.logistics.insert(Logistic(id, name, count_sent, count_received))

    repo.get_conn().commit()


def main(args):
    initiate(args)
    order(sys.argv)
    Repository.repo.get_conn().commit()


if __name__ == '__main__':
    main(sys.argv)
