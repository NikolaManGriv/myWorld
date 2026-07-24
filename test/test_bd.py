import errors as e
import dataBase as db
import pytest


def test_search():
    print("="*10)
    print("Search for one movie that exists")
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    bd_tst.set_query("harry potter 1")
    
    cant= bd_tst.search_db ()
    assert(cant[1] > 0)
    print("Success :D")
    print("="*10)

def test_search_not_found():
    print("="*10)
    print("Search for one movie that does not exist")
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    bd_tst.set_query("harry potter 3")
    
    cant= bd_tst.search_db ()
    assert(cant[1] == 0)
    print("Success :D")
    print("="*10)

def test_change_lt1():
    print("="*10)
    print("change a movie that has cantidad = 0")
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    
    bd_tst.set_query("harry potter 2")
    cantidad= bd_tst.search_db()
    
    assert(cantidad[1]>0)
    
    bd_tst.change_db()
    cant_new= bd_tst.search_db ()
    
    assert(cantidad[0] == cant_new[0] and cant_new[0] == 0)
    print("Success :D")
    print("="*10)

def test_change_gt1():
    print("="*10)
    print("change a movie that has cantidad >= 1")
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    
    bd_tst.set_query("lotr 1")
    cantidad= bd_tst.search_db()
    
    assert(cantidad[1]>0)
    
    bd_tst.change_db()
    cant_new= bd_tst.search_db ()
    
    assert(cantidad[0] == cant_new[0] +1)
    print("Success :D")
    print("="*10)

def test_multiple_name():
    print("="*10)
    print("search cantidad from a lot of movies")
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    
    bd_tst.set_query("harry potter")
    cantidad= bd_tst.search_db()
    
    assert(cantidad[1] == 2)
    assert(cantidad[0] == 3) 
    
    print("Success :D")
    print("="*10)

def test_name_not_set():
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    
    with pytest.raises(e.Error_name_not_set):
        cant= bd_tst.search_db ()


def test_invalid_name():
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    
    with pytest.raises(e.Error_invalid_name):
        bd_tst.set_query ()


def test_unnespecific_name():
    bd_tst= db.my_db("test1.duckdb", "test1.csv")
    
    with pytest.raises(e.Error_movie_unnspecific):
        bd_tst.set_query ("harry potter")
        bd_tst.change_db()


#TODO test de los errores

if __name__ == "__main__":
    test_invalid_name()
    test_name_not_set()
    test_unnespecific_name()
    test_search()
    test_search_not_found()
    test_change_gt1()
    test_change_lt1()
    test_multiple_name()