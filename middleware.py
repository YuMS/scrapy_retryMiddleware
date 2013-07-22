# -*- coding: utf-8 -*-


from scrapy import log
from scrapy.contrib.downloadermiddleware.retry \
    import RetryMiddleware


class RetryRecordMiddleware(RetryMiddleware):

    def __init__(self, settings):
        RetryMiddleware.__init__(self, settings)

    def process_exception(self, request, exception, spider):
        to_return = RetryMiddleware.process_exception(
            self, request, exception, spider)
        retries = request.meta.get('retry_times', 0) + 1
        log.msg('retries time is %s %d' % (retries, retries))
        log.msg('max_retry_times is %d' % self.max_retry_times)
        if retries > self.max_retry_times and request.meta.get('status', 0) == 2:
            key, value = request.meta.get('pair', ('', ''))
            key = key.strip()
            value = value.strip()
            log.msg('recording failed pair %s\t%s' % (key, value))
            of = open('check/failed.txt', 'a')
            of.write('%s\t%s\n' % (key, value))
            of.close()
        return to_return
