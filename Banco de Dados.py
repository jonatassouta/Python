import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-9SPM9G4\SQLEXPRESS;'
                      'Database=TesteBDPython;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM TesteBDPython.dbo.Pessoas')

for row in cursor:
    print(row)