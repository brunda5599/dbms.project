import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="Brunda@123", host="127.0.0.1", port="5432")


cur = conn.cursor()

cur.execute("SELECT PROD, DEP, QUANTITY  from STOCK")
rows = cur.fetchall()
for row in rows:
    print("PROD = ", row[0])
    print("DEP = ", row[1])
    print("QUANTITY = ", row[2], "\n")
print("Operation done successfully")
conn.close()