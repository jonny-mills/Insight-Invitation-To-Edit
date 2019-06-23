#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:47:02 2019

"""
import lxml.etree
import lxml.html
import requests
import os

master_urls = []
urls = {'March_clickstream':'https://dumps.wikimedia.org/other/clickstream/2019-03/clickstream-enwiki-2019-03.tsv.gz','Feb_clickstream':'https://dumps.wikimedia.org/other/clickstream/2019-02/clickstream-enwiki-2019-02.tsv.gz','Jan_clickstream':'https://dumps.wikimedia.org/other/clickstream/2019-01/clickstream-enwiki-2019-01.tsv.gz'}

for month, url in urls.items():
    print(url)
    os.system("curl -o " + month + ".gz " + url) 
    os.system("gunzip -k " + month +'.gz') #tell terminal to gunzip the file
    #os.system("aws s3 cp " + month + " s3://wiki-data-123456") #tell terminal to put the data to S3
    os.system('rm ' + month+'.gz')
    os.system('rm ' + month)


