# -*- coding:utf-8 -*-
from bson import Regex

__author__ = 'JRoger'

from pymongo import Connection, MongoClient
from bson.objectid import ObjectId


class WorkLogRepository(object):
    def __init__(self):
        self.conn = MongoClient(host='127.0.0.1', port=27017, max_pool_size=100)
        self.db = self.conn.WorkLogDB

    def add(self, item):
        self.db.worklog.insert(item)

    def find(self, page_size, page_index, keyword=None):
        reg = None
        cursor = None
        total = 0
        if keyword is not None:
            reg = Regex(r'%s' % keyword)
            cursor = self.db.worklog\
                .find({'$or': [{'title': reg}, {'content': reg}]})\
                .sort("creationdate", -1)\
                .skip((page_index - 1) * page_size)\
                .limit(page_size)
            total = self.db.worklog\
                .find({'$or': [{'title': reg}, {'content': reg}]})\
                .count()
        else:
            cursor = self.db.worklog.find().sort("creationdate", -1).skip((page_index - 1) * page_size).limit(page_size)
            total = self.db.worklog.count()
        return cursor, total

    def update(self, modify_id, fields):
        # 在使用 update 时，比如要更新的字段有三个，分别为 title, content, date, 如果不带 $set，并执行更新 title, 则会将
        # content, date 设置为空，即不带 $set 每次都会更新整条记录
        # 如果带上 $set 则只会更新要更新的 title 字段，而不会影响 content, date 原来的值
        result = self.db.worklog.update({'_id': ObjectId(modify_id)}, {'$set': fields}, manipulate=False)
        if result['nModified'] == 1:
            return 1
        else:
            return -1

    def disconnection(self):
        self.conn.disconnect()