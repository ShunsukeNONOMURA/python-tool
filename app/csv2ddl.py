from converter import *

# 前処理
path_csv = 'table.csv'
df = pd.read_csv(path_csv)
df['key'] = df['key'].str.lower()

# 設定
schema_name = 'tmp'
table_name = schema_name+'.'+path_csv.split('.')[0]
table_pkay_name = path_csv.split('.')[0] + '_pkey'

# ddl出力
ddl = Converter.df2ddl(
    df,
    table_name,
    table_pkay_name,
)
print(ddl)

# export records csv
df_records = Converter.df2df_records(
    df,
)
print(df_records)
path_records_csv = 'table_records.csv'
df_records.to_csv(path_records_csv, index=False)
