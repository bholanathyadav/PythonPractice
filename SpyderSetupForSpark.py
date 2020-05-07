# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:37:04 2019

@author: CA DHEERAJ
"""

import os
import sys
os.chdir("C:/Users/CA DHEERAJ/PycharmProjects/BNY/SparkProgs")
os.curdir

# Configure the environment. Set this up to the directory where
# Spark is installed
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = 'C:/Spark'
    
# Create a variable for our root path
SPARK_HOME = os.environ['SPARK_HOME']

# Add the following paths to the system path. Please check your 
# installation to make sure these zip files actually exis. The names 
# might change as versions change.

sys.path.insert(0,os.path.join(SPARK_HOME, "python"))
sys.path.insert(0,os.path.join(SPARK_HOME, "python", "lib"))
sys.path.insert(0,os.path.join(SPARK_HOME, "python", "lib", "pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME, "python", "lib", "py4j-0.10.7-src.zip"))

# Initiate Spark Context. Once this is done all applications can run
from pyspark import SparkContext
from pyspark import SparkConf

# Optionally configure Spark settings
conf = SparkConf()
conf.set("spark.executor.memory", "1g")
conf.set("spark.cores.max", "2")

conf.setAppName("Bhola")

# Initialize SparkContext. Run only once. Otherwise you get
# Context Error.

sc = SparkContext('local', conf=conf)

# Test to make sure everything works.
lines = sc.textFile("auto-data.csv")
lines.count()