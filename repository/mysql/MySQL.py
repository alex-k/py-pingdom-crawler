from repository.Repository import Repository
import mysql.connector


class MySQL(Repository):
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='root',
            password='root',
            database='uptime_test',
            host='127.0.0.1'
        )
        self.cursor = self.cnx.cursor()
    
    def get_all_checks(self):
        query = "select check_id from checks limit 5"
        self.cursor.execute(query)
        data = []
        for (check_id) in self.cursor:
            data.append("{}".format(check_id))
        return data
    
    def get_statistic(self, check_id, timestamp):
        # type: (int, int) -> object
        query = "select check_id from checks where check_id={} and timestamp={}"
        self.cursor.execute(query, (check_id, timestamp))
        data = self.cursor.fetchone()
        print data
        return data
