from pyspark.sql import DataFrameWriter
import os

class PostgresConnector(object):
    def init(self):
        self.database_name = 'my_db1'
        self.hostname = 'ec2-52-37-38-224.us-west-2.compute.amazonaws.com'
        self.url_connect = "jdbc:postgresql://{hostname}:5431/{db}".format(hostname=self.hostname, db=self.database_name)
        self.properties = {"user":"test1",

                 # "password":os.environ['POSTGRES_PASS'],
                  "password" : "test1",
                  "driver": "org.postgresql.Driver"

                 }
def get_writer(self, df):
    return DataFrameWriter(df)

def write(self, df, table, md):
    my_writer = self.get_writer(df)
    #my_writer.jdbc(self.url_connect, table, self.properties)
    print ("@@@@@@@@@@@@@@@@@@@@ table = ", table, "@@@@@@ u= ", self.url_connect)
    df.write.jdbc(url=self.url_connect,table= table,mode=md,properties=self.properties)
