import sqlite3

sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

db = sqlite3.connect('test.db')
db.cursor()
db.cursor().execute(sql_create_projects_table )