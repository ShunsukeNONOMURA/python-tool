import os
from pydantic import BaseModel

import pandas as pd


"""
CREATE TABLE テーブル名
(列名 データ型 (データ長) [列制約],
,
,
CONSTRAINT table_pkey PRIMARY KEY (ID)
)
"""

def csv2ddl(path_csv, table_name=''):
    df = pd.read_csv(path_csv)

    if table_name == '':
        table_name = path_csv.split('.')[0]

    ddl = f'CREATE TABLE {table_name} (\n'

    for index,item in df.iterrows():
        ddl += f'{item.key} {item.type}'
        if index != df.index[-1]: 
            ddl += ','
        ddl += '\n'

    ddl += ')'

    return ddl

ddl = csv2ddl('table.csv')
print(ddl)
