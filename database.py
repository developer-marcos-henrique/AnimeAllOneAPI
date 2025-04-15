# database controller
import sqlite3

class sqlController:
    def __init__(self, consult_content: str):
        self.consult_content = consult_content
    
    def __enter__(self):
        self.connection = sqlite3.connect("cache.db")
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.commit()
        self.connection.close()

    def cacheAdressCheck(self) -> tuple:
        search = "SELECT * FROM cacheAdress WHERE search LIKE ?"
        
        x = self.cursor.execute(
            search, (f"%{self.consult_content}%",)
        ).fetchone()
        
        return x if x != None else False
    
    def getCachedContent(self, id_adress):
        getCache = "SELECT * FROM cache WHERE id_adress=?"
        
        x = self.cursor.execute(
            getCache, (id_adress)
        ).fetchone()
        
        return x if x != None else False
    

    def insertInto(self, table, cache_data: tuple):
        self.cursor.execute(f"INSERT INTO {table} VALUES (?, ?, ?)", (cache_data))

    
    def storeFromJson(self):
        # to store data from a json file, use this scheme
        # {
        #   "shows": {[
        #       {data},
        #       {data},
        #       ....
        #   ]}
        # }
        pass


# with sqlController("amo,e00") as x:
#     x.insertInto(table="cache",
#                     cache_data=(
#                         6,
#                         '{"x":1, "y":2, "z":3}',
#                         '{"x":1, "y":2, "z":3}'
#                     )
#                 )