#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding: UTF-8
# time 2018-11-17
# Author fcj
# message 领英redis数据缓存

import json
from datetime import timedelta
from redis import StrictRedis


class RedisCache:
    def __init__(self, client=None, expires=timedelta(days=30), encoding='utf-8'):
        self.client = StrictRedis(host='localhost', port=6379, db=0) if client is None else client
        self.expires = expires
        self.encoding = encoding

    def __getitem__(self, url):
        record = self.client.get(url)
        if record:
            return json.loads(record.decode(self.encoding))
        else:
            raise KeyError(url + 'does not exist')

    def __setitem__(self, url, result):
        data = bytes(json.dumps(result), self.encoding)
        self.client.setex(url, self.expires, data)


# if __name__ == '__main__':
#     cache = RedisCache(expires=timedelta(seconds=20))
#     cache['test'] = {'html': '...', 'code': 200, 'url': 'www.baidu.com'}
#     print(cache.client.get('test'))
#     print(cache.client.get('tt'))