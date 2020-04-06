from model.DomainInfo import DomainInfo

from pyspark.sql import SparkSession

from pyspark.sql.types import *  # Necessary for creating schemas
from pyspark.sql.functions import * # Importing PySpark functions

spark = SparkSession.builder.appName('Basics').master("local[1]").getOrCreate()

def domain_info(domain_name):
    d = DomainInfo(domain_name)
    return [d.get_domain_age_in_days(), d.get_domain_registrar(), d.get_domain_expiration()]


a_list = [(1, 'www.microsoft.com'), (2, 'www.google.com'), (3, 'www.facebook1234512345.com')]


domain_info_udf = udf(domain_info, StructType(
    [
        StructField("domain_age", LongType(), True),
        StructField("domain_registrar", StringType(), True),
        StructField("domain_expiration", StringType(), True)
    ]))

df = spark.createDataFrame(a_list, ['id', 'domain_name'])

df = df.select("id", "domain_name", domain_info_udf("domain_name").alias("domain_info"))

df = df.select("id", "domain_name",
               df["domain_info.domain_age"], df["domain_info.domain_registrar"], df["domain_info.domain_expiration"])

df.show()

