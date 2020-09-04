import sys
sys.path.append("/spark/python")
from pyspark import SparkConf, SparkContext

conf = SparkConf()
conf.setAppName("very-cool-test-app")
conf.setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rdd = sc.parallelize(a)
    rdd2 = rdd.map(lambda x: x * 2)
    print(rdd2.collect())
