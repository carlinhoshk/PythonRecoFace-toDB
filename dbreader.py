import pandas as pd
import sqlite3

df = pd.read_sql_query("SELECT * FROM faces", sqlite3.connect("faces.db"))

print(df)