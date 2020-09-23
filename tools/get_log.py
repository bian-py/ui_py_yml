import logging.handlers


class GetLog:
    __logger = None

    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            #             获取日志器
            cls.__logger = logging.getLogger()
            # 修改默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename='./log/hmtt.log',
                                                           when='midnight',
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')

            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器中
            th.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.__logger.addHandler(th)
        return cls.__logger

if __name__ == "__main__":
    log = GetLog.get_logger()
    log.info("信息级别日志")
    log.error("错误级别日志")
