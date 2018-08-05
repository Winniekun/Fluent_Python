'''
@author  : kongweikun
@file    : logging.py
@time    : 18-7-19 下午4:03
@contact : kongwiki@163.com
'''
import  logging
import logging.config

# logging.warning('Watch out!')
# logging.info('I told you so')
# logging.basicConfig(filename='example.log',level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

# logging.config.fileConfig('logging.conf')
#
# # create logger
# logger = logging.getLogger('simpleExample')
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')
service_name = "KongWiki"

logger = logging.getLogger("AppName")
logger.error('%s service is down!', service_name)  # 使用logger的格式化，推荐
logger.error('%s service is %s!', service_name, 'down')  # 多参数格式化
logger.error('{} service is {}!'.format(service_name, 'down')) # 使用format函数，推荐