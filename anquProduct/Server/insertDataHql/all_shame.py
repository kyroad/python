#encodig=utf-8
# _*_ coding:utf-8 _*_
# Writer : lgy
# dateTime : 2016-07-25

from pyspark.sql.types import StructType,StructField,IntegerType,StringType,LongType
from pyspark.sql import Row


searchApp_shame = StructType([
	StructField("word", StringType(), True),
	StructField("priority",StringType(),True),
	StructField("searchApp", StringType(), True),
	StructField("searchCount",StringType(),True),
	StructField("genre",StringType(),True),
	StructField('type',StringType(),True),
	StructField("time",StringType(),True)
	])

_categry_shame = StructType([StructField("genreID",StringType(),True),
	StructField("cName",StringType(),True),
	StructField("url",StringType(),True),
	StructField("parentID",StringType(),True),
	StructField("weight",StringType(),True)])

hintWord_shame = StructType([StructField('word',StringType(),True),
	StructField('priority',StringType(),True),
	StructField('type',StringType(),True),
	StructField('hintWord',StringType(),True),
	StructField('time',StringType(),True)])

thinkWord_shame =  StructType([StructField('hintWord',StringType(),True),])