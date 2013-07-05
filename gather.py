#!/usr/bin/env python2.7
"""
gather.py
By Simon Pratt

Gather information about hacker news
"""

import httplib
import sys
import json

connection = httplib.HTTPConnection('api.ihackernews.com')
connection.request('GET','http://api.ihackernews.com/page')
res = connection.getresponse()

if res.status != 200:
    sys.exit(1)

data = res.read()
ob = json.loads(data)
for item in ob['items']:
    print '{0}: {1}'.format(item['title'].encode('ascii','ignore'), item['points'])
sys.exit(0)
