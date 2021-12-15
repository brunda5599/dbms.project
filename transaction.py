import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="Brunda@123")


#For isolation: SERIALIZABLE
conn.set_isolation_level(3)
#For atomicity
conn.autocommit = False

try:

    cur = conn.cursor()
    cur.execute("UPDATE PRODUCT set PROD = 'PP1' where PROD = 'P1'")
#ALTER TABLE PRODUCT RENAME COLUMN phone TO contact_phone;
    conn.commit()
    print("Total number of rows updated :", cur.rowcount)

    cur.execute("SELECT PROD, PNAME, PRICE  from PRODUCT")
    rows = cur.fetchall()
    for row in rows:
        print("PROD = ", row[0])
        print("PNAME = ", row[1])
        print("PRICE = ", row[2], "\n")

    cur.execute("SELECT PROD, DEP, QUANTITY  from STOCK")
    rows = cur.fetchall()
    for row in rows:
        print("PROD = ", row[0])
        print("DEP = ", row[1])
        print("QUANTITY = ", row[2], "\n")

    print("Operation done successfully")



except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    conn.rollback()
finally:
    if conn:
        conn.commit()
        cur.close
        conn.close
        print("PostgreSQL connection is now closed")