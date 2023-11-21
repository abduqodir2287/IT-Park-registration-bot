import sqlite3


class Itpark_bot_helperDB:
    def __init__(self, dbname='tech.db'):
        self.dbname = dbname
        self.tabname = ''
        self.conn = sqlite3.connect(self.dbname)

    def create_table(self, tabname='custom'):
            """
            create table for database
            :param tabname: base name
            :return: default table name id, username
            """
            self.tabname = tabname
            sql = f"""
                CREATE TABLE IF NOT EXISTS {tabname}(
                      "id"  INTEGER PRIMARY KEY AUTOINCREMENT,
                      "fullname" TEXT, 
                      "phoneNumber" TEXT,
                      "course"  TEXT, 
                      "pasport" TEXT
                    );"""

            self.conn.execute(sql)

    def add_item(self, fullname, phoneNumber, course, pasport):

        sql = f"""INSERT INTO "{self.tabname}" (fullname, phoneNumber, course, pasport)
            VALUES (?, ?, ?, ?);"""
        data = (fullname, phoneNumber, course, pasport)
        self.conn.execute(sql, data)
        self.conn.commit()


    def delete_item(self, id):
        sql = f"""DELETE FROM {self.tabname} where id=={id};"""
        self.conn.execute(sql)
        self.conn.commit()

    def select_item(self):
        sql = f"""SELECT * FROM {self.tabname};"""
        return self.conn.execute(sql).fetchall()

    def update_item(self, id, username):
        sql = f"""UPDATE {self.tabname} SET 
                username={username}, 
                WHERE id={id};"""

        self.conn.execute(sql)
        self.conn.commit()

    def log_out(self):
        self.conn.close()
