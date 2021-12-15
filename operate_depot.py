import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="Brunda@123", host="127.0.0.1", port="5432")


cur = conn.cursor()

cur.execute("SELECT DEP, ADDR, VOLUME  from DEPOT")
rows = cur.fetchall()
for row in rows:
    print("DEP = ", row[0])
    print("ADDR = ", row[1])
    print("VOLUME = ", row[2], "\n")

print("Operation done successfully")
conn.close()
