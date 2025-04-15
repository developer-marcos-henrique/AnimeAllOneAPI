# scrap controller
import sqlite3
from database import sqlController
from plugins import scrap_data
class process:
    def __init__(self, user_input: str):
        self.user_input = user_input

    def start(self):
        with sqlController(self.user_input) as cache:
            cache_result = cache.cacheAdressCheck()
        
            if cache_result != False: # if search is cached on db
                return cache.getCachedContent(cache_result[1])
            
            
            

        


print(process("anime").start())



#sqlController(consult_content="anime").doSearch