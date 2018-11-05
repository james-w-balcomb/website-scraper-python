import datetime
import email
# import time

from datetime import datetime
from email.utils import parsedate


def convert_to_http_date_format(date_time):
    # def httpdate(dt)
    # https://stackoverflow.com/questions/225086/rfc-1123-date-representation-in-python
    # A manual way to format it which is identical with wsgiref.handlers.format_date_time is:
    """Return a string representation of a date according to RFC 1123
    (HTTP/1.1).

    The supplied date must be in UTC.

    """
    weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][date_time.weekday()]

    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
             "Oct", "Nov", "Dec"][date_time.month - 1]

    # TODO(JamesBalcomb): refactor to .format() syntax
    http_date = "%s, %02d %s %04d %02d:%02d:%02d GMT" % (weekday,
                                                         date_time.day,
                                                         month,
                                                         date_time.year,
                                                         date_time.hour,
                                                         date_time.minute,
                                                         date_time.second)

    return http_date

# You can use wsgiref.handlers.format_date_time from the stdlib
#  which does not rely on locale settings
#
# from wsgiref.handlers import format_date_time
# from datetime import datetime
# from time import mktime
#
# now = datetime.now()
# stamp = mktime(now.timetuple())
# print format_date_time(stamp) #--> Wed, 22 Oct 2008 10:52:40 GMT
# You can use email.utils.formatdate from the stdlib which does not rely on locale settings
#
# from email.utils import formatdate
# from datetime import datetime
# from time import mktime
#
# now = datetime.now()
# stamp = mktime(now.timetuple())
# print formatdate(
#     timeval     = stamp,
#     localtime   = False,
#     usegmt      = True
# ) #--> Wed, 22 Oct 2008 10:55:46 GMT

# http://code.activestate.com/recipes/577015-parse-http-date-time-string/
# This recipe will help you parse datetime strings returned by HTTP servers
#  following the RFC 2616 standard (which supports three datetime formats).


def parse_http_datetime(s):
    # from datetime import datetime
    # from email.utils import parsedate
    return datetime(*parsedate(s)[:6])


def convert_http_date_to_mysql_timestamp(http_date):
    # def convert_http_date_gmt_to_mysql_timestamp_local(http_date):

    # http_header_date = requests_response.headers.get('date')  # <class 'str'>
    # >>> http_header_date: Thu, 25 Oct 2018 19:15:38 GMT

    # http_header_date = datetime.datetime\
    #     .strptime(http_header_date, '%a, %d %b %Y %H:%M:%S %z')\
    #     .strftime('%Y-%m-%d %H:%M:%S.%f')
    # ValueError: time data
    #  'Thu, 25 Oct 2018 22:29:55 GMT' does not match format '%a, %d %b %Y %H:%M:%S %z'

    # datetime.datetime.strptime(http_header_date, '%a, %d %b %Y %H:%M:%S GMT')

    print("mysql_timestamp: {}".format(str(http_date)))

    date_time = email.utils.parsedate_to_datetime(http_date)

    print("mysql_timestamp: {}".format(str(date_time)))

    mysql_timestamp = date_time.replace(tzinfo = datetime.timezone.utc).astimezone(tz = None)

    print("mysql_timestamp: {}".format(str(mysql_timestamp)))

    return mysql_timestamp
