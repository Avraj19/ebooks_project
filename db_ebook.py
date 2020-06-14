import pydoc

class Ebooks_db():

    def __init__(self, database='Northwind', server='databases2.spartaglobal.academy', username='SA',
                 password='Passw0rd2018'):
        # 1) DB server connection variables
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn = self._establish_conn()
        self.cursor = self.conn.cursor()