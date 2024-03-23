# import sqlite3
#
# con = sqlite3.connect("")
# c = con.cursor()
#
#
# c.execute("""CREATE TABLE rajma (
#             name TEXT,
#             age INTEGER,
#             height REAL
#     )""")
#
# con.commit()
#
# all_students = [
#     ('john', 21, 1.8),
#     ('david', 35, 1.7),
#     ('michael', 19, 1.83),
# ]
# c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)
# con.commit()
