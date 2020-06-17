import logging

import logging.handlers


class Logger:
    def __init__(self, path='./logs/ip_pool.log', c_level=logging.DEBUG, f_level=logging.INFO):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(c_level)

        # 设置文件日志
        fh = logging.handlers.TimedRotatingFileHandler(path, when='D', interval=1, backupCount=5)
        fh.setFormatter(fmt)
        fh.setLevel(f_level)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


log = Logger()
