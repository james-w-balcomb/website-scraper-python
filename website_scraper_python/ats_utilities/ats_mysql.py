import logging

import pymysql


# logger = logging.getLogger(__name__)
# logger.addHandler(logging.NullHandler)


TINYINT_SIGNED_MINIMUM = -128
TINYINT_SIGNED_MAXIMUM = 128
TINYINT_UNSIGNED_MINIMUM = 0
TINYINT_UNSIGNED_MAXIMUM = 255
SMALLINT_SIGNED_MINIMUM = -32768
SMALLINT_SIGNED_MAXIMUM = 32767
SMALLINT_UNSIGNED_MINIMUM = 0
SMALLINT_UNSIGNED_MAXIMUM = 65535
MEDIUMINT_SIGNED_MINIMUM = -8388608
MEDIUMINT_SIGNED_MAXIMUM = 8388607
MEDIUMINT_UNSIGNED_MINIMUM = 0
MEDIUMINT_UNSIGNED_MAXIMUM = 16777215
INT_SIGNED_MINIMUM = -2147483648
INT_SIGNED_MAXIMUM = 2147483647
INT_UNSIGNED_MINIMUM = 0
INT_UNSIGNED_MAXIMUM = 4294967295
BIGINT_SIGNED_MINIMUM = -9223372036854775808
BIGINT_SIGNED_MAXIMUM = 9223372036854775807
BIGINT_UNSIGNED_MINIMUM = 0
BIGINT_UNSIGNED_MAXIMUM = 18446744073709551615
DECIMAL_DIGITS_MINIMUM = 1
DECIMAL_DIGITS_MAXIMUM = 65
DECIMAL_PLACES_MINIMUM = 0
DECIMAL_PLACES_MAXIMUM = 30

SQL_CHECK_FOR_DATABASE = \
    "SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = '{}';"
SQL_CHECK_FOR_TABLE = \
    "SELECT TABLE_NAME FROM information_schema.TABLES" \
    " WHERE TABLE_SCHEMA = {} AND TABLE_NAME = {};"
SQL_CREATE_DATABASE = \
    "CREATE DATABASE `{}`;"
SQL_CREATE_TABLE_TOP = \
    "CREATE TABLE `{}`.`{}` ("
SQL_CREATE_TABLE_MIDDLE = \
    "`{}` {} {} COMMENT '{}',"
SQL_CREATE_TABLE_BOTTOM = \
    ") ENGINE={} DEFAULT CHARSET={} COLLATE={} COMMENT '{}' ;"
SQL_DROP_DATABASE = \
    "DROP DATABASE `{}`;"
SQL_DROP_TABLE = \
    "DROP TABLE `{}`.`{}`;"
SQL_INSERT = \
    "INSERT INTO `{}`.`{}` (%) VALUES (%);"
SQL_INSERT_INTO_VALUES = \
    "INSERT INTO `{}`.`{}` ({}) VALUES ({});"
SQL_USE_DATABASE = \
    "USE `{}`;"
SQL_SELECT_ALL = \
    "SELECT * FROM `{}`.`{}` ORDER BY NULL"


def create_mysql_schema(mysql_cursor, schema_name):

    # # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    # TODO(JamesBalcomb): Add check for DROP; (!?not sure if I originally had a reason not to?!)
    # TODO(JamesBalcomb): add check for illegal characters
    # TODO(JamesBalcomb): add check for unsafe characters

    query_results = mysql_cursor.execute(SQL_CHECK_FOR_DATABASE.format(schema_name))
    logger.debug("query_results: {}".format(str(query_results)))

    if not query_results:
        query_results = mysql_cursor.execute(SQL_CREATE_DATABASE.format(schema_name))
        logger.debug("query_results: {}".format(str(query_results)))
    else:
        query_results = mysql_cursor.execute(SQL_DROP_DATABASE.format(schema_name))
        logger.debug("query_results: {}".format(str(query_results)))
        query_results = mysql_cursor.execute(SQL_CREATE_DATABASE.format(schema_name))
        logger.debug("query_results: {}".format(str(query_results)))

    return query_results


def create_mysql_table(mysql_cursor,
                       storage_engine_name,
                       character_set_name,
                       collation_name,
                       table_comment,
                       schema_name,
                       table_name,
                       field_names,
                       columns_datatypes):
    # create_mysql_table_with_defaults(
    #                    schema_name,
    #                    table_name,
    #                    column_names,
    #                    column_datatypes,
    #                    column_options,
    #                    column_comments
    # )
    # create_mysql_table_with_defaults_from_sequence(
    #                    schema_name,
    #                    table_name,
    #                    list/tuple(column_names, column_datatypes, column_options, column_comments)
    # )

    # # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    sql_create_table_top = SQL_CREATE_TABLE_TOP.format(table_name)
    sql_create_table_middle = str()
    sql_create_table_bottom = SQL_CREATE_TABLE_BOTTOM.format(storage_engine_name,
                                                             character_set_name,
                                                             collation_name,
                                                             table_comment)

    for field_name in field_names:
        sql_create_table_middle = sql_create_table_middle + \
                                  SQL_CREATE_TABLE_MIDDLE.format(
                                      field_name,
                                      columns_datatypes[field_name]
                                  )

    sql_create_table = \
        sql_create_table_top + \
        sql_create_table_middle.rstrip(',') + \
        sql_create_table_bottom

    query_results = mysql_cursor.execute(SQL_USE_DATABASE.format(schema_name))
    logger.debug("query_results: {}".format(str(query_results)))

    query_results = mysql_cursor.execute(SQL_CHECK_FOR_TABLE.format(schema_name, table_name))
    logger.debug("query_results: {}".format(str(query_results)))

    if not query_results:
        query_results = mysql_cursor.execute(sql_create_table)
        logger.debug("query_results: {}".format(str(query_results)))
    else:
        query_results = mysql_cursor.execute(SQL_DROP_TABLE.format(schema_name, table_name))
        logger.debug("query_results: {}".format(str(query_results)))
        query_results = mysql_cursor.execute(sql_create_table)
        logger.debug("query_results: {}".format(str(query_results)))

    return query_results


def do_mysql_insert(mysql_cursor, schema_name, table_name, columns, values):
    """

    :param mysql_cursor:
    :param schema_name:
    :param table_name:
    :param columns: list/tuple of column names
    :param values: list/tuple of values
    :return:
    """
    # # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    sql_insert_query = "INSERT INTO {}.{} (".format(schema_name, table_name)

    for element in columns:
        sql_insert_query = sql_insert_query + element + ","

    sql_insert_query = sql_insert_query.rstrip(",")

    sql_insert_query = sql_insert_query + ") VALUES ("

    placeholders = len(columns) * "%s,"

    sql_insert_query = sql_insert_query + placeholders

    sql_insert_query = sql_insert_query.rstrip(",")

    sql_insert_query = sql_insert_query + ")"
    # print("sql_insert_query: {}".format(sql_insert_query))

    # print("SQL_INSERT_INTO_VALUES: " + SQL_INSERT_INTO_VALUES.format(schema_name,
    #                                                                  table_name,
    #                                                                  columns,
    #                                                                  values))

    # query_results = mysql_cursor.execute(SQL_INSERT_INTO_VALUES.format(schema_name,
    #                                                                    table_name,
    #                                                                    columns,
    #                                                                    values))

    query_results = mysql_cursor.execute(sql_insert_query, values)
    logger.debug("query_results: {}".format(str(query_results)))

    return query_results


def get_mysql_connection(configuration):
    # mysql_connection = pymysql.connect(
    #     host = None,
    #     user = None,
    #     password = "",
    #     database = None,
    #     port = 0,
    #     unix_socket = None,
    #     charset = '',
    #     sql_mode = None,
    #     read_default_file = None,
    #     conv = None,
    #     use_unicode = None,
    #     client_flag = 0,
    #     cursorclass = Cursor,
    #     init_command = None,
    #     connect_timeout = 10,
    #     ssl = None,
    #     read_default_group = None,
    #     compress = None,
    #     named_pipe = None,
    #     autocommit = False,
    #     db = None,
    #     passwd = None,
    #     local_infile = False,
    #     max_allowed_packet = 16 * 1024 * 1024,
    #     defer_connect = False,
    #     auth_plugin_map = None,
    #     read_timeout = None,
    #     write_timeout = None,
    #     bind_address = None,
    #     binary_prefix = False,
    #     program_name = None,
    #     server_public_key = None
    # )

    # # logger = logging.getLogger(__name__)
    # logger = logging.getLogger('default_logger')

    # logger.debug("mysql_connection = pymysql.connect("
    #              "host = {}, "
    #              "port = {}, "
    #              "user = {}, "
    #              "passwd = {}, "
    #              "charset = {}, "
    #              "use_unicode = {})".format(
    #                 configuration["mysql"]["host"],
    #                 int(configuration["mysql"]["port"]),
    #                 configuration["mysql"]["user"],
    #                 configuration["mysql"]["passwd"],
    #                 configuration["mysql"]["charset"],
    #                 configuration["mysql"]["use_unicode"]))

    mysql_connection = pymysql.connect(
        host = configuration["mysql"]["host"],
        port = int(configuration["mysql"]["port"]),
        user = configuration["mysql"]["user"],
        passwd = configuration["mysql"]["passwd"],
        db = configuration["mysql"]["db"],
        charset = configuration["mysql"]["charset"],
        use_unicode = configuration["mysql"]["use_unicode"],
        autocommit = configuration["mysql"]["autocommit"]
    )
    # KeyError: 'host'
    # pymysql.err.OperationalError: (1045,
    #  "Access denied for user 'WebSiteScraper'@'localhost' (using password: YES)")

    # mysql_connection.max_allowed_packet = 1024
    # Disable / Enable autocommit Manually
    # mysql_connection.autocommit(True)

    return mysql_connection


def get_mysql_cursor(mysql_connection):

    # # logger = logging.getLogger(__name__)
    # logger = logging.getLogger('default_logger')

    # mysql_cursor = mysql_connection.cursor(prepared = True)
    # TypeError: cursor() got an unexpected keyword argument 'prepared'

    # A buffered cursor fetches and buffers the rows of a result set after executing a query;
    #  see Section 10.6.1, “cursor.MySQLCursorBuffered Class”.)
    # This way, it is unnecessary to fetch the rows in a new variables.
    #  Instead, the cursor can be used as an iterator.
    # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursorbuffered.html
    # ...need to set buffered=True to avoid MySQL Unread result error...
    # mysql_cursor = mysql_connection.cursor(buffered = True)

    mysql_cursor = mysql_connection.cursor()

    # mysql_cursor.execute('SET NAMES utf8mb4')
    # mysql_cursor.execute('SET CHARACTER SET utf8mb4')
    # mysql_cursor.execute('SET character_set_connection=utf8mb4')

    return mysql_cursor


def set_mysql_schema(mysql_cursor, schema_name):

    # # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    query_results = mysql_cursor.execute(SQL_USE_DATABASE.format(schema_name))
    logger.debug("query_results: {}".format(str(query_results)))

    return query_results
