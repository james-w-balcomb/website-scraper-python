import datetime
import inspect
import logging
import sys


# logger = logging.getLogger(__name__)
# logger.addHandler(logging.NullHandler)


def log_variable(variable_name, variable):
    # ats_utilities.log.log_variable(variable_name = "file_path", variable = file_path)

    # # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    logger.debug("{}: (type: {}); (length: {}); (value: {})".format(
        variable_name,
        str(type(variable)),
        str(len(str(variable))),
        str(variable)))

    return None


def log_csv_dict_reader(csv_dict_reader_instance):

    # # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    csv_reader__dialect = csv_dict_reader_instance.dialect
    csv_reader__fieldnames = csv_dict_reader_instance.fieldnames
    csv_reader__line_num = csv_dict_reader_instance.line_num
    csv_reader__reader = csv_dict_reader_instance.reader
    csv_reader__restkey = csv_dict_reader_instance.restkey
    csv_reader__restval = csv_dict_reader_instance.restval

    logger.debug("csv.DictReader: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_dict_reader_instance)),
        str(len(str(csv_dict_reader_instance))),
        str(csv_dict_reader_instance)))

    logger.debug("csv.DictReader.dialect: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_reader__dialect)),
        str(len(str(csv_reader__dialect))),
        str(csv_reader__dialect)))

    logger.debug("csv.DictReader.fieldnames: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_reader__fieldnames)),
        str(len(str(csv_reader__fieldnames))),
        str(csv_reader__fieldnames)))

    logger.debug("csv.DictReader.line_num: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_reader__line_num)),
        str(len(str(csv_reader__line_num))),
        str(csv_reader__line_num)))

    logger.debug("csv.DictReader.reader: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_reader__reader)),
        str(len(str(csv_reader__reader))),
        str(csv_reader__reader)))

    logger.debug("csv.DictReader.restkey: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_reader__restkey)),
        str(len(str(csv_reader__restkey))),
        str(csv_reader__restkey)))

    logger.debug("csv.DictReader.restval: (type: {}); (length: {}); (value: {})".format(
        str(type(csv_reader__restval)),
        str(len(str(csv_reader__restval))),
        str(csv_reader__restval)))

    return None


def log(message):
    # noinspection PyProtectedMember
    frame_name = sys._getframe().f_back.f_code.co_name

    print("[{0:%Y-%m-%dT%H:%M:%S.%f%Z}] [{1}] {2}"
          .format(datetime.datetime.now(), frame_name, message))
    sys.stdout.flush()


def print_debug(function_name, message):
    print("[{0:%Y-%m-%dT%H:%M:%S.%f%Z}] [{1}] {2}"
          .format(datetime.datetime.now(), function_name, message))
    sys.stdout.flush()


def print_debug_and_exit(function_name, message):
    print_debug(function_name, message)
    print("Exiting...")
    sys.stdout.flush()
    sys.exit("Mistakes were made.")


# noinspection PyUnusedLocal
def get_caller_name_1():

    getframe_expr = 'sys._getframe({}).f_code.co_name'
    caller = eval(getframe_expr.format(2))
    callers_caller = eval(getframe_expr.format(3))

    current_frame = inspect.currentframe()
    calling_frame = inspect.getouterframes(current_frame, 2)

    # inspect.stack() can incur heavy performance overhead
    # don't retrieve a list of all the stack frames
    caller_name = inspect.stack()[1][3]

    # noinspection PyProtectedMember
    frame_name = sys._getframe().f_back.f_code.co_name

    # avoids ...
    # "hidden" methods
    # potentially deprecated methods
    # numerical indexing into the stack
    frame_name = inspect.currentframe().f_code.co_name

    return caller


def get_caller_name_2(skip=2):
    """Get a name of a caller in the format module.class.method

       `skip` specifies how many levels of stack to skip while getting caller
       name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.

       An empty string is returned if skipped levels exceed stack height
    """

    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
        return ''
    parent_frame = stack[start][0]

    frame_names = []
    module = inspect.getmodule(parent_frame)
    # `modname` can be None when frame is executed directly in console

    if module:
        frame_names.append(module.__name__)
    # detect classname
    if 'self' in parent_frame.f_locals:
        # I don't know any way to detect call from the object method
        # XXX: there seems to be no way to detect static method call - it will
        #      be just a function call
        frame_names.append(parent_frame.f_locals['self'].__class__.__name__)
    code_name = parent_frame.f_code.co_name
    if code_name != '<module>':  # top level usually
        frame_names.append(code_name)  # function or a method

    # # Avoid circular refs and frame leaks
    #   https://docs.python.org/2.7/library/inspect.html#the-interpreter-stack
    del parent_frame, stack

    return ".".join(frame_names)


def what_is_my_name():
    # https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
    print(inspect.stack()[0][0].f_code.co_name)
    print(inspect.stack()[0][3])
    print(inspect.currentframe().f_code.co_name)
    # noinspection PyProtectedMember
    print(sys._getframe().f_code.co_name)
    # Note that the inspect.stack calls are thousands of times slower than the alternatives:
    # $ python -m timeit -s 'import inspect, sys' 'inspect.stack()[0][0].f_code.co_name'
    # 1000 loops, best of 3: 499 usec per loop
    # $ python -m timeit -s 'import inspect, sys' 'inspect.stack()[0][3]'
    # 1000 loops, best of 3: 497 usec per loop
    # $ python -m timeit -s 'import inspect, sys' 'inspect.currentframe().f_code.co_name'
    # 10000000 loops, best of 3: 0.1 usec per loop
    # $ python -m timeit -s 'import inspect, sys' 'sys._getframe().f_code.co_name'
    # 10000000 loops, best of 3: 0.135 usec per loop
    # ...
    # ...[option 3] hundreds of times faster than options 1 and 2...
    # ... found option 3 three times faster than option 4


def initialize_logging():
    # Log Levels: NOTSET (0), DEBUG (10), INFO (20), WARN (30), ERROR (40), CRITICAL (50)
    # logger = logging.getLogger()  # root logger
    logger = logging.getLogger('default_logger')
    logger.setLevel(logging.DEBUG)

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create file handler for EVERYTHING (NOTSET)
    fh_notset = logging.FileHandler('./log/csv_to_mysql.log')
    fh_notset.setLevel(logging.NOTSET)

    # create file handler for DEBUG
    fh_debug = logging.FileHandler('./log/debug.log')
    fh_debug.setLevel(logging.DEBUG)

    # create file handler for INFO
    fh_info = logging.FileHandler('./log/info.log')
    fh_info.setLevel(logging.INFO)

    # create file handler for WARN
    fh_warn = logging.FileHandler('./log/warn.log')
    fh_warn.setLevel(logging.WARN)

    # create file handler for ERROR
    fh_error = logging.FileHandler('./log/error.log')
    fh_error.setLevel(logging.ERROR)

    # create file handler for CRITICAL
    fh_critical = logging.FileHandler('./log/critical.log')
    fh_critical.setLevel(logging.CRITICAL)

    # create formatter and add it to the handlers
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] "
                                  "[%(name)s] [%(module)s] [%(funcName)s] "
                                  "%(message)s")
    fmt_extreme = logging.Formatter(
        "[%(asctime)s]"
        " [%(levelname)s] [%(name)s] [%(filename)s] [%(lineno)d] [%(module)s] [%(funcName)s]"
        " [%(process)d] [%(processName)s] [%(thread)d] [%(threadName)s]"
        " %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S%z"
    )
    ch.setFormatter(formatter)
    fh_notset.setFormatter(formatter)
    fh_debug.setFormatter(fmt_extreme)
    fh_info.setFormatter(formatter)
    fh_warn.setFormatter(formatter)
    fh_error.setFormatter(formatter)
    fh_critical.setFormatter(formatter)

    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh_notset)
    logger.addHandler(fh_debug)
    logger.addHandler(fh_info)
    logger.addHandler(fh_warn)
    logger.addHandler(fh_error)
    logger.addHandler(fh_critical)

    return logger


# def setup_logging_ini()
#     pass


# def setup_logging_json(default_path='logging.json',default_level=logging.INFO,env_key='LOG_CFG'):
#     """Setup logging configuration
#
#     """
#     # import os
#     # import json
#     # import logging.config
#     path = default_path
#     value = os.getenv(env_key, None)
#     if value:
#         path = value
#     if os.path.exists(path):
#         with open(path, 'rt') as f:
#             config = json.load(f)
#         logging.config.dictConfig(config)
#     else:
#         logging.basicConfig(level=default_level)


# def setup_logging_yaml(default_path='logging.yaml',default_level=logging.INFO,env_key='LOG_CFG'):
#     """Setup logging configuration
#
#     """
#     import os
#     import logging
#     import logging.config
#     import yaml
#     path = default_path
#     value = os.getenv(env_key, None)
#     if value:
#         path = value
#     if os.path.exists(path):
#         with open(path, 'rt') as f:
#             config = yaml.safe_load(f.read())
#         logging.config.dictConfig(config)
#     else:
#         logging.basicConfig(level=default_level)
