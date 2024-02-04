import sqlite3
class sqlEasyFlask:
    def __init__(self, g, route) -> None:
        # Get the global app value
        # g is an object used from Flask
        self.g = g
        self.route = route
    
    def get_db(self):
        db = getattr(self.g,'db',None)
        if db is None:
            # Init database
            db = self.g.db = sqlite3.connect(self.route,isolation_level=None)
            # Autocommit for values as INSERT and DELETE
            
            # Get rows in dict way
            db.row_factory = sqlite3.Row
        return db
    
    def close_db(self):
        db = getattr(self.g,'db',None)
        if db is not None:
            db.close()

    def query(self, query,*args,one=False):
        ''' Query will be the usual query from sqlite
            Args are the arguments the query needs that are ?
            If one true, then only one row will be displayed'''
        cur = self.get_db().execute(query,args)
        rowsValues = cur.fetchall()
        cur.close()
        return (rowsValues[0] if rowsValues else None) if one else rowsValues