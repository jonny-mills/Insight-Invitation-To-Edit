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
url = 'https://dumps.wikimedia.org/other/clickstream/2019-04/'
page = requests.get(url)
root = lxml.html.fromstring(page.content)
links_raw = root.xpath('//a/@href')
urls = [url+i for i in links_raw if 'clickstream-enwiki' in i]
url = urls[0]
os.system("curl -o clickstream.gz " + url) 
os.system("gunzip -k " + "clickstream.gz") #tell terminal to gunzip the url
os.system('aws s3 cp clickstream_april s3://wiki-data-123456') #tell terminal to put the data to S3
#os.system('rm clickstream')