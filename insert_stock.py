import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="Brunda@123", host="127.0.0.1", port="5432")

#inserting data into stock
cur = conn.cursor()

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P1', 'D1', 1000 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P1', 'D2', -100 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P1', 'D4', 1200 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P3', 'D1', 3000 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P3', 'D4', 2000 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P2', 'D4', 1500 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P2', 'D1', -400 )");

cur.execute("INSERT INTO STOCK(PROD,DEP,QUANTITY) \
     VALUES('P2', 'D2', 2000 )");

conn.commit()
print("Records created successfully")
conn.close()


