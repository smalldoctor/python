# -*- coding: utf-8

from threading import Lock
import time


class Throttle:
    def __init__(self, rate):
        self._comsume_lock = Lock()
        #  速率
        self.rate = rate
        # token数量
        self.tokens = 0
        # 最后补充时间
        self.last = 0

    def comsume(self, amount=1):
        with self._comsume_lock:
            now = time.time()

            # 时间测量在第一令牌请求上初始化以避免初始突发
            if self.last == 0:
                self.last = now

            elapsed = now - self.last

            # 请确保传递时间的量足够大以添加新的令牌
            # 进行token的补充
            if int(elapsed * self.rate):
                self.tokens += int(elapsed * self.rate)
                self.last = now

            # 不要过度填满桶;
            #  补充的token不能多余速率的阀值；此处速率是每秒多少
            self.tokens = (
                self.rate
                if self.tokens > self.rate
                else self.tokens
            )

