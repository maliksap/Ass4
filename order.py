import sys

from datetime import datetime

import Repository
from Vaccine import Vaccine


def total(list1):
    inventory = 0
    for vaccine in list1:
        inventory = inventory + vaccine[0]
    return inventory


def order_by_date(date):
    return date[1]


def order(args):
    repo = Repository.repo
    file1 = open(args[3], 'w')

    with open(args[2], 'r') as orders_file:
        cnfg_list = orders_file.read().splitlines()
        cur = repo.get_conn().cursor()
        for line in cnfg_list:
            recive_or_send = line.split(",")
            # recive
            if len(recive_or_send) > 2:
                cur.execute("""SELECT id FROM suppliers WHERE name=?""", [recive_or_send[0]])
                supplier_id = cur.fetchone()[0]
                vac_id = repo.get_vaccines().get_num_of_vaccines()
                repo.vaccines.insert(Vaccine(vac_id, recive_or_send[2], supplier_id, recive_or_send[1]))

                cur.execute("""SELECT logistic FROM suppliers WHERE id=?""", [supplier_id])
                logistic_id = cur.fetchone()[0]
                cur.execute("""SELECT count_received FROM logistics WHERE id=?""", [logistic_id])
                curr_count_received = cur.fetchone()[0]
                cur.execute("""UPDATE logistics SET count_received=? WHERE id=?""",
                            [curr_count_received + int(recive_or_send[1]), logistic_id])

            # send
            elif len(recive_or_send) == 2:
                amount = int(recive_or_send[1])
                while amount > 0:
                    cur.execute("""SELECT * FROM vaccines""")
                    vaccines = cur.fetchall()
                    swap_seperators(vaccines)
                    vaccine = sorted(vaccines, key=lambda vaccines: datetime.strptime(vaccines[1], '%Y-%m-%d'))
                    vaccine = vaccines.pop(0)
                    quantity_of_vaccine = vaccine[3]
                    if quantity_of_vaccine > amount:
                        cur.execute("""UPDATE vaccines SET quantity=? WHERE id=?""",
                                    [quantity_of_vaccine - amount, vaccine[0]])
                        amount = 0
                    else:
                        cur.execute("""DELETE FROM vaccines WHERE id=?""", [vaccine[0]])
                        amount = amount - quantity_of_vaccine
                    repo.get_conn().commit()
                cur.execute("""SELECT logistic FROM clinics WHERE location=?""", [recive_or_send[0]])
                logistic_id = cur.fetchone()[0]
                cur.execute("""SELECT count_sent FROM logistics WHERE id=?""", [logistic_id])
                curr_count_sent = cur.fetchone()[0]
                cur.execute("""UPDATE logistics SET count_sent=? WHERE id=?""",
                            [curr_count_sent + int(recive_or_send[1]), logistic_id])
                cur.execute("""SELECT demand FROM clinics WHERE location=?""", [recive_or_send[0]])
                demand = cur.fetchone()[0]
                cur.execute("""UPDATE clinics SET demand=? WHERE location=?""",
                            [demand - int(recive_or_send[1]), recive_or_send[0]])
            cur.execute("""SELECT quantity FROM vaccines""")
            inventory = cur.fetchall()
            cur.execute("""SELECT demand FROM clinics""")
            demands = cur.fetchall()
            cur.execute("""SELECT count_sent FROM logistics""")
            sent = cur.fetchall()
            cur.execute("""SELECT count_received FROM logistics""")
            received = cur.fetchall()

            file1.write(str(total(inventory))+","+str(total(demands))+","+str(total(received))+","+str(total(sent))+"\n")


def swap_seperators(lst):
    """
    lst is either a list of list, or a list of tuples.
    will return a a list of list/tuple where all − occurrences been replaced with - .
    This also replace the lst inplace.
    """
    for j, l in enumerate(lst):
        nl = list(l)
        for i, v in enumerate(nl):
            if isinstance(v, str):
                nl[i] = v.replace('−', '-')
        lst[j] = nl if isinstance(l, list) else tuple(nl)
    return lst
    # ***

