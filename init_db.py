import duckdb

conn = duckdb.connect("base1.duckdb")
conn.execute("CREATE TABLE IF NOT EXISTS pelis AS SELECT * FROM 'bd1.csv'")
conn.close()
print("base1.duckdb created.")
