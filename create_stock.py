import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="Brunda@123", host="127.0.0.1", port="5432")


cur = conn.cursor()
cur.execute('''CREATE TABLE STOCK
      (PROD TEXT     references PRODUCT(PROD) ON DELETE CASCADE ON UPDATE CASCADE,
      DEP           TEXT    references DEPOT(DEP) ON DELETE CASCADE,
      QUANTITY            INT     NOT NULL);''')
print("Table created successfully")
conn.commit()
conn.close()

