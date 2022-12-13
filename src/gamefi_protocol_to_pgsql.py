import psycopg2
from configparser import ConfigParser
from sys import argv
from src.getContracts import getContracts


class PostgreSQLPipeline(object):
    def check_version(self, db_creds):
        # 建立连接
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])

        # 使用cursor()方法创建游标对象
        cursor = conn.cursor()
        # 使用execute()方法执行MYSQL函数
        cursor.execute("select version()")
        # 使用fetchone()方法获取单行。
        data = cursor.fetchone()
        print("Connection established to: ", data)
        # 关闭连接
        conn.close()

    def normal_add(self, db_creds):
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        try:
            cur = conn.cursor()  # 游标
            # self.conn.query(sql_desc)
            #cur.execute("INSERT INTO ewrrw values(dict(item));")
            print("begin INSERT")
            command = "INSERT INTO gamefi_contract_collection(chain, contract_address, protocol_slug) VALUES('{chain}', '{addr}', '{slug}');".format(
                chain='BNB Chain', addr='0x0627578d5d388e6ea417080461303af575d3eba2', slug='mobox')

            print(command)
            cur.execute(command)
            conn.commit()

            print("Data added to PostgreSQL database!")

        except Exception:
            print('insert record into table failed')
            print(Exception)
        conn.close()

    def process_items(self, db_creds, items):
        # sql_desc="INSERT INTO table_name(xxx, yyy)values(item['xxx'],item['yyy'])"
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        i = 0
        try:
            cur = conn.cursor()
            # self.conn.query(sql_desc)
            #cur.execute("INSERT INTO ewrrw values(dict(item));")
            
            while i< len(items):
                item = items[i]
                i+=1
                command = "INSERT INTO gamefi_contract_collection(chain, contract_address, protocol_slug) VALUES('{chain}', '{addr}', '{slug}');".format(
                    chain=item['chain'], addr=item['contract_address'], slug=item['protocol_slug'])
                cur.execute(command)
                # print("No."+i+"  "+command)
            conn.commit()

            # print("Data added to PostgreSQL database!")

        except Exception:
            print('insert record into table failed')
            print(Exception)

        
        finally:
            if cur:
                cur.close()

        cur.close()
        # return item


if __name__ == '__main__':
    # Read and parse configurations
    config = ConfigParser()  # 解析config
    try:
        config.read(f'config/{argv[1]}.conf')  # dev configuration

    except IndexError:
        print("Command should be of type: python <start file> <config name>. Example: python main.py local")
        exit()
    db_creds = config['DB_CREDS']
    # Get the contracts list from json file

    pgsqlPipeline = PostgreSQLPipeline()
    print("----------------------------------------------")
    contracts = getContracts(slug=argv[2])
    print("----------------------------------------------")
    pgsqlPipeline.process_items(db_creds=db_creds, items=contracts)
