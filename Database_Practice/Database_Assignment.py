
import sqlite3

conn = sqlite3.connect('Assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filename TEXT)')
    conn.commit()

conn = sqlite3.connect('Assignment.db')

# Tuple of File List:

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# This is a loop that goes through each object in the above tuple to find the files that end in .txt

for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # (x) will now hold the value of the two files in the tuple above that end with .txt
            cur.execute('INSERT INTO tbl_files (col_filename) VALUES (?)', (x,))
            # The .txt files will now be in our database in TABLE (tbl_files) under the COLUMN (col_filename)
            print(x)
            # This will Print the two .txt files in the Python Shell
conn.close()
