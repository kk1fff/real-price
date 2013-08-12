#!/usr/bin/env python

import sys, pymongo, re
from pymongo.uri_parser import parse_uri

uri = sys.argv[1]
filename = sys.argv[2]

f = open(filename, 'r')
client = pymongo.MongoClient(uri)
db = client[parse_uri(uri)['database']]

collection = db['schools']
pattern = re.compile(r"[^,]*,[^,]*,([^,]*),([^,]*),([^,]*),[^,]*,([^,]*),([^,]*),[^,]*,[^,]*,([^,]*),([^,]*)$")
while True:
    line = f.readline()
    if line == '':
        break
    m = pattern.match(line)
    if m != None:
        collection.insert({
            'school_type': m.group(1),
            'fund_type': m.group(2),
            'city': m.group(3),
            'name': m.group(4),
            'addr': m.group(5),
            'latitude': float(m.group(6)),
            'longitude': float(m.group(7))
        });
