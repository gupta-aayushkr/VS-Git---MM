from pyspark.sql import *
#from lib.logger import Log4j

if __name__ == "main":
    Spark = SparkSession().builder \
    .appname("Hello Spark") \
    .master("Local[3]") \
    .getOrcreate()

    #logger = Log4j(Spark)
    #logger.info("Starting HelloSpark")
    #logger.info("Finished HelloSpark")
    Spark.stop()