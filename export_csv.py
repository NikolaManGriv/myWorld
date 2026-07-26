import duckdb

conn = duckdb.connect("base1.duckdb")
conn.execute("COPY pelis TO 'new.csv' (HEADER, DELIMITER ',')")
conn.close()
print("new.csv created.")
