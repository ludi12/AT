# coding=utf8

import logging

def log_init():
    """
    设置日志格式
    :return:
    """

    # 获取日志对象
    logger = logging.getLogger()
    # 设置日志对象的日志级别
    logger.setLevel(level=logging.INFO)

    # 创建FileHandler对象,设置日志写到哪里
    handler = logging.FileHandler(r"log\test.log", 'a')

    handler.setLevel(logging.INFO)
    # Formatter对象代表日志的格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 设置日志的格式
    handler.setFormatter(formatter)

    # 把FileHandler对象添加到日志对象
    logger.addHandler(handler)
