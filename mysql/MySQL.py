from db.Db import Db


class MySQL(Db):
    def select_column_from_table(self, table_name, column_name):
        return [1, 2, 22]
