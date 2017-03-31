#coding:utf-8
import os,sys,time,re,csv
import log,logger
import log,logger

import imputil
from uiautomator import Device
import traceback
import log,logging
import multiprocessing


def finddevices():
    # rst = util.exccmd('adb devices')
    rst = imputil.exccmd('adb devices')
    devices = re.findall(r'(.*?)\s+device',rst)
    if len(devices) >1:
        deviceIds = devices[1:]
        logger.info('共找到%s个手机'%str(len(devices)-1))
        for i in deviceIds:
            logger.info('ID为%s'%i)
        return deviceIds
    else:
        logger.error('没有找到手机，请检查')
        return