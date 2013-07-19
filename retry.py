from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware


class RetryRecordMiddleware(RetryMiddleware):

    def __init__(self):
        RetryMiddleware.__init(self)

    def process_exception(self, request, exception, spider):
        RetryMiddleware.process_exception(self, request, exception, spider)
        retries = request.meta.get('retry_times', 0) + 1
        if retries > self.max_retry_times:
            key, value = request.meta.get('pair', ('', ''))
            key = key.strip()
            value = value.strip()
            open('check/failed', 'a').write('%s\t%s\n' % (key, value))
