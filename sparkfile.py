# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:27:07 2020

@author: Behnaz
"""


"""
#sparkshell
python3 -m venv venv
. venv/bin/activate
cd /usr/hdp/current/spark2-client/bin
pyspark --jars "/root/mongo-hadoop-spark-2.0.2.jar" --driver-class-path "/root/mongo-java-driver-3.4.3.jar"  --packages org.mongodb.spark:mongo-spark-connector_2.11:2.3.2
"""
from pyspark import SparkContext,SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import six
import pandas

## reading from mongo
conf = SparkConf().set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.3.2")
spark = SparkSession.builder.appName("myApp").config("spark.mongodb.input.uri", "mongodb://127.0.0.1/market_db.market_collection").config("spark.mongodb.output.uri", "mongodb://127.0.0.1/market_db").getOrCreate()
df = spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()

## selecting desired columns
final_df = df.select("High","Open","Price","Volume","Change %","Low","Date")
final_df = final_df.withColumnRenamed("Change %", "Change")


final_df.show()

## removing M and % in change and volume columns
df_converted = df_converted.withColumn('Volume', regexp_replace('Volume','M', ''))
df_converted = df_converted.withColumn('Change', regexp_replace('Change','%', ''))

## type casting for proper data types
df_converted = final_df.withColumn ("Price", df["Price"].cast(FloatType()))
df_converted = final_df.withColumn ("Low", df["Low"].cast(FloatType()))
df_converted = final_df.withColumn ("High", df["High"].cast(FloatType()))
df_converted = final_df.withColumn ("Open", df["Open"].cast(FloatType()))
df_converted = final_df.withColumn ("Change", df["Change"].cast(FloatType()))
df_converted = final_df.withColumn ("Volume", df1["Volume"].cast(FloatType()))
df_converted = final_df.withColumn ("Date", df1["Date"].cast(DateType()))


final_df.dtypes

