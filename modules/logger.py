from conf import setting
import logging,os
def logs_make():
    logger = logging.getLogger()
    # 用于写入日志文件
    fh = logging.FileHandler('%s%s%s.log' % (setting.log_path(),os.sep,setting.log_type()))

    # 用于输出到控制台
    ch = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')

    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)   # logger对象可以添加多个fh和ch对象
    logger.addHandler(ch)
    logger.setLevel(setting.loggerLevel)
    return logger
Log = logs_make()