import duckdb

conn = duckdb.connect()
conn.execute("""
    COPY (
        SELECT * FROM 'new.csv'
        UNION ALL
        SELECT * FROM 'other.csv'
        WHERE titulo NOT IN (SELECT titulo FROM 'new.csv')
    ) TO 'merged.csv' (HEADER, DELIMITER ',')
""")
conn.close()
print("merged.csv created.")
