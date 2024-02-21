# -*- coding: utf-8 -*-

import os
import pymongo


mongo_uri = os.environ.get('DB_URI')
mongo_db = 'db'
mongo_collection = 'proxy'

# 连接到MongoDB数据库
client = pymongo.MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

# 查询数据
query = {"status": 1}
projection = {"_id": 0, "ip": 1, "port": 1, "type": 1}
results = collection.find(query, projection)

# 输出查询结果
type_file_map = {
    '1': 'http.txt',
    '2': 'https.txt',
    '3': 'socks4.txt',
    '4': 'socks5.txt'
}
for result in results:
    data = result['ip'] + ':' + result['port']
    proxy_type = str(result['type'])

    file_name = type_file_map[proxy_type]
    with open(file_name, "a") as file:
        file.write(data + "\n")
