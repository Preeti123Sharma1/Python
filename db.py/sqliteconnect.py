import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
    create table student(
        st_id INT AUTO_INCREMENT PRIMARY KEY,
        st_name varchar(50),
        st_class varchar(50),
        st_email varchar(30)
    )

''')
conn.close()