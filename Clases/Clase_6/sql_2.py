# -*- coding: utf-8 -*-


import pandas as pd
from sqlalchemy import create_engine, event
from urllib.parse import quote_plus


con = "Driver={SQL Server};Server=LAPTOP-RP1INROE\SQLEXPRESS;Database=SQL;Trusted_Connection=yes"
quoted = quote_plus(con)
new_con = 'mssql+pyodbc:///?odbc_connect={}'.format(quoted)
engine = create_engine(new_con)
df = pd.read_excel('Monedas.xlsx')
df.loc[101:200,:].to_sql('Monedas', con = engine, if_exists = 'append',index = False)

pd.read_sql('select * from monedas',engine)
