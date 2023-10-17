
import pandas as pd

class Converter:
    @staticmethod
    def df2ddl(df, table_name, table_pkay_name):
        ddl = ''
        ddl += f'CREATE TABLE {table_name} (\n'

        # Table
        for index,item in df.iterrows():
            len_str = f'({round(item.len)})' if not pd.isnull(item.len) else ''
            required_str = ' NOT NULL' if item.required == '〇' else ''
            ddl += f'{item.key} {item.type}{len_str}{required_str}'
            ddl += ',\n'

        ## PK
        df_pk = df[df['pk'] == '〇']
        pks = ','.join([item.key for index,item in df_pk.iterrows()])
        ddl += f'CONSTRAINT {table_pkay_name} PRIMARY KEY({pks})\n'
        ddl += ');\n'

        # comment
        ddl_comments = ''
        for index,item in df.iterrows():
            ddl_comments += f"COMMENT ON COLUMN {table_name}.{item.key} IS '{item.comment}';\n" if not pd.isnull(item.comment) else ''
        ddl += '\n' + ddl_comments

        return ddl
    
    @staticmethod
    def df2df_records(df):
        columns = [item.key for index,item in df.iterrows()]
        return pd.DataFrame(columns = columns)