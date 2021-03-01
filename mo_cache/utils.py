# -*- coding: utf-8 -*-
from hashlib import md5
import pickle


def get_md5(byte_array):
    """获取md5 only Python3"""
    return md5(byte_array).hexdigest()


def get_params_sign(*args, **kwargs):
    """获取参数唯一值"""
    params = pickle.dumps(args) + pickle.dumps(kwargs)
    return get_md5(params)


def get_func_name(func):
    """获取函数的名称"""
    return func.__module__ + '.' + func.__name__


if __name__ == '__main__':
    print(get_params_sign('hi'))
    print(get_func_name(get_func_name))
