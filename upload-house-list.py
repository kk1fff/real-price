#!/usr/bin/env python

import sys, pymongo, re
from pymongo.uri_parser import parse_uri

uri = sys.argv[1]
filename = sys.argv[2]

f = open(filename, "r");
client = pymongo.MongoClient(uri)
db = client[parse_uri(uri)['database']]
collection = db['houses']

pattern = re.compile(r"([^,]*),[^,]*,([^,]*),[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,([^,]*),[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,([^,]*),([^,]*)$");
while True:
    line = f.readline()
    if line == '':
        break
    m = pattern.match(line)
    if (m != None) and (m.group(5).strip() != ""):
        collection.insert({
            'dist': m.group(1), # dist
            'addr': m.group(2), # addr
            'type': m.group(3),
            'latitude': float(m.group(4)),
            'longitude': float(m.group(5))
        });
