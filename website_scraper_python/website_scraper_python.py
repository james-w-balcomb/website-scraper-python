import logging
import pickle
import requests
import sys

from ats_utilities import ats_configuration
from model.bigstub import BigStub
from mysql_connection_manager import MysqlConnectionManager

TEST_RUN = False
SAVE_FILE = True


def main(sys_argv):
    # logger = logging.getLogger(__name__)
    logger = logging.getLogger('default_logger')

    configuration = ats_configuration.get_configuration(sys_argv)

    MysqlConnectionManager(host = configuration["mysql"]["host"],
                           port = int(configuration["mysql"]["port"]),
                           user = configuration["mysql"]["user"],
                           passwd = configuration["mysql"]["passwd"],
                           db = configuration["mysql"]["db"])

    if TEST_RUN:
        file_path = "C:\\Development\\website-scraper-python\\_research\\bigstub\\python-requests-get\\"
        file_name = "pickled_requests_response.pickle"
        file_handle = open(file_path + file_name, "rb")
        requests_response = pickle.load(file_handle)
    else:
        url = "https://www.bigstub.com/chicago-il-events.aspx"
        requests_response = requests.get(url)
        if SAVE_FILE:
            file_path = "C:\\Development\\website-scraper-python\\_research\\bigstub\\python-requests-get\\"
            file_name = "pickled_requests_response.pickle"
            file_handle = open(file_path + file_name, "wb")
            pickle.dump(requests_response, file_handle)
            file_handle.close()

    requests_response_text = requests_response.text
    #   <class 'str'>

    big_stub = BigStub(requests_response_text)
    #   <class 'model.bigstub.BigStub'>

    big_stub.process_upcoming_events_list_items()


if __name__ == '__main__':
    main(sys.argv)
