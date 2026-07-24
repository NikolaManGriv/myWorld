import streamlit
import duckdb as duck
import errors as e 

class my_db:
    def __init__(self, bd_name= "base1.duckdb", data= "bd1.csv"):
        self.conn= duck.connect(bd_name)
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS pelis AS SELECT * FROM {data}")
        self.query: str = None
        self.search= "SELECT cantidad FROM pelis WHERE titulo ILIKE ?"
        self.change= "UPDATE pelis SET cantidad = cantidad - 1 WHERE titulo ILIKE ? AND cantidad >0"

    def set_query(self, q:str= None):
        if not q or len(q) == 0:
            raise e.Error_invalid_name()
        self.query= f"%{q.lower()}%"

    def search_db(self):
        if not self.query:
            raise e.Error_name_not_set()

        res= self.conn.execute(self.search, [self.query]).fetchall()

        return sum( [i[0] for i in res]), len(res)

    def change_db(self):
        if not self.query:
            raise e.Error_name_not_set()

        _, cant = self.search_db()
        if cant != 1:
            raise e.Error_movie_unnspecific()

        self.conn.execute(self.change, [self.query])
        

    def close_db(self):
        self.conn.close()

if __name__ == "__main__":
    db= my_db()
    db.set_query("harry potter 1")
    cant= db.search_db ()
    print(cant)
    db.change_db()
    cant= db.search_db ()
    print(cant)
    """
    db.set_query("harry potter")
    cant2= db.search_db ()

    print(cant2)
    """