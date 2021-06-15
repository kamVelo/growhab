import sqlite3 as sql
conn = sql.connect('test.db')
cursor = conn.cursor()

"""
cursor.execute('''
INSERT INTO LEDON (LEDon) VALUES('HIGH')
''')
conn.commit()
"""
output = cursor.execute('''
SELECT * FROM LEDON
''').fetchall()
print(output[0][0])