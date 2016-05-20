# -*- coding: utf-8 -*-

# https://uqer.io/labs/notebooks/Untitled.nb

import quartz
from quartz.api import *

import pandas as pd
import numpy as np
from datetime import datetime    
from matplotlib import pylab


# 回测起始时间
start = '2010-01-12'
# 回测结束时间
end = '2014-12-31'
# 策略参考标准
benchmark = 'HS300'
# 证券池，支持股票和基金
universe = ['000005.XSHE','000048.XSHE','000417.XSHE','000516.XSHE','000705.XSHE',\
            '000850.XSHE','000877.XSHE','002051.XSHE','002085.XSHE','002137.XSHE',\
           '002173.XSHE','002221.XSHE','002227.XSHE','002229.XSHE','002250.XSHE',\
           '002272.XSHE','002287.XSHE','002310.XSHE','300035.XSHE','600048.XSHG',\
           '600060.XSHG','600073.XSHG','600083.XSHG','600106.XSHG','600162.XSHG',\
           '600208.XSHG','600220.XSHG','600240.XSHG','600252.XSHG','600327.XSHG',\
           '600587.XSHG','600594.XSHG','600695.XSHG','600790.XSHG','601007.XSHG',]
# 起始资金
capital_base = 26420
# 策略类型，'d'表示日间策略使用日线回测
freq = 'd'
# 调仓频率，表示执行handle_data的时间间隔，由于freq = 'd'，时间间隔的单位为交易日
refresh_rate = 10000

# 初始化虚拟账户状态
def initialize(account):
    pass

# 每个交易日的买入卖出指令
def handle_data(account):
    for stock in account.universe:
        order(stock,100)
