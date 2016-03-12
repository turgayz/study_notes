# coding: utf-8
import pyspark as ps
sc = ps.SparkContext()

%save spark1 1-10

sc.master --> u'local[*]'
shows the master attribute
