import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="Brunda@123", host="127.0.0.1", port="5432")

#inserting data into product
cur = conn.cursor()

cur.execute("INSERT INTO PRODUCT (PROD,PNAME,PRICE) \
     VALUES ('P1', 'TAPE', 2.5 )");

cur.execute("INSERT INTO PRODUCT (PROD,PNAME,PRICE) \
    VALUES ('P2', 'TV', 250 )");

cur.execute("INSERT INTO PRODUCT (PROD,PNAME,PRICE) \
     VALUES ('P3', 'VER', 80 )");
conn.commit()
print("Records created successfully")
conn.close()