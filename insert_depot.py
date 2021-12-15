import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="Brunda@123", host="127.0.0.1", port="5432")

#inserting data into depot
cur = conn.cursor()

cur.execute("INSERT INTO DEPOT(DEP,ADDR,VOLUME) \
     VALUES('D1', 'NEWYORK', 9000 )");

cur.execute("INSERT INTO DEPOT(DEP,ADDR,VOLUME) \
     VALUES('D2', 'SYRACUSE', 6000 )");

cur.execute("INSERT INTO DEPOT(DEP,ADDR,VOLUME) \
     VALUES('D4', 'NEWYORK', 2000 )");
conn.commit()
print("Records created successfully")
conn.close()