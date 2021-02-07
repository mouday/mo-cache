# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals


class CacheAbstract(object):
    """统一的接口
    备注：delete、clear删除动作较为危险，不进行具体实现
    """

    def set(self, key, value, expire=-1):
        """设置取值"""
        raise NotImplementedError()

    def get(self, key):
        """获取值"""
        raise NotImplementedError()
