import datetime
import re
import requests
import sys

from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

from ats_utilities import ats_mysql
from model.bigstub_event import BigStubEvent
from model.htmldocument import HtmlDocument
from mysql_connection_manager import MysqlConnectionManager

REGEX_UPCOMING_EVENTS_EVENT_ID = ".*\?event_id\=([0-9]*).*"
REGEX_UPCOMING_EVENTS_TITLE_EVENT_COUNT = "([0-9].*) Upcoming Events:"
REGEX_BIGSTUB_DATETIME_FORMAT_1 = "^(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2}$"
REGEX_BIGSTUB_DATETIME_FORMAT_2 = "^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) [0-9]{1,2}, [0-9]{4}$"
SQL_INSERT_INTO_BIGSTUB_SCRAPER_CHICAGO_IL_EVENTS = "INSERT INTO " \
                                                "website_scraper.bigstub_chicago_il_events " \
                                                "(" \
                                                "event_datetime, " \
                                                "event_url, " \
                                                "event_id, " \
                                                "event_name, " \
                                                "event_venue_name, " \
                                                "event_venue_city, " \
                                                "event_venue_state, " \
                                                "record_ts" \
                                                ") " \
                                                "VALUES " \
                                                "(" \
                                                "%s, %s, %s, %s, %s, %s, %s, %s" \
                                                ");"


class BigStub(HtmlDocument):

    uri_scheme = "https"
    uri_authority = ""
    uri_path = "chicago-il-events.aspx"
    uri_query = None
    uri_fragment = None
    uri_hostname = "www.bigstub.com"
    uri_port = 80
    uri_user = None
    uri_pass = None
    url = "https://www.bigstub.com/chicago-il-events.aspx"
    mysql_schema_name = "website_scraper"
    mysql_table_name = "bigstub_chicago_il_events"

    # def __init__(self, requests_response_text):
    #     self.requests_response_text = requests_response_text
    #     super(BigStub, self).__init__(requests_response_text)
    #     self.upcoming_events_list_html = self.get_upcoming_events_list_html()

    # def __init__(self, *args, **kwargs):
    #     super(BigStub, self).__init__(*args, **kwargs)
    #     self.upcoming_events_list_html = self.get_upcoming_events_list_html()

    # def __init__(self, *args, **kwargs):
    #     super(self.__class__, self).__init__(*args, **kwargs)
    #     self.upcoming_events_list_html = self.get_upcoming_events_list_html()

    def get_upcoming_events_list_html(self):
        
        upcoming_events_list_html = self.soup.find(id = 'upcomingEventsList')
        
        return upcoming_events_list_html

    def get_upcoming_event_list_title_html(self):
        
        upcoming_event_list_title_html = self.soup.find(id = 'upcomingEventsTitle')
        
        return upcoming_event_list_title_html

    def get_upcoming_events_count(self):
        
        upcoming_events_title_text_string = self.soup.find(id = 'upcomingEventsList').find(id = 'upcomingEventsTitle').div.div.h3.string.strip()
        
        re_search = re.search(REGEX_UPCOMING_EVENTS_TITLE_EVENT_COUNT, upcoming_events_title_text_string)
        
        upcoming_events_count = re_search.group(1).strip()
        
        return upcoming_events_count
    
    def get_upcoming_events_list_items(self):
        
        upcoming_events_list_items = self.soup.find(id = 'upcomingEventsList').find_all("div", {"class": "item2 row"})
        
        return upcoming_events_list_items

    def get_event_datetime_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        upcoming_events_list_item_ue_date_contents = upcoming_events_list_item.find("div", {"class": "ueDate small-3 medium-2 columns"}).contents
        
        upcoming_events_list_item_ue_date_time = upcoming_events_list_item_ue_date_contents[2]
        
        time_and_day_period = upcoming_events_list_item_ue_date_time
        
        event_time_string = "{time_and_day_period}".format(time_and_day_period = time_and_day_period.strip())
        
        if event_time_string == "Time TBA":
            event_time_string = "1:11 AM"
        
        upcoming_events_list_item_ue_date_span_contents = upcoming_events_list_item.find("div", {"class": "ueDate small-3 medium-2 columns"}).span.contents
        
        month_name_and_day = upcoming_events_list_item_ue_date_span_contents[0]
        
        event_date_string = "{month_name_and_day}".format(month_name_and_day = month_name_and_day.strip()).strip()
        
        if re.match(REGEX_BIGSTUB_DATETIME_FORMAT_1, event_date_string):
            bigstub_event_datetime_format_string = "%B %d %Y %I:%M %p"
            need_to_add_current_year = True
        elif re.match(REGEX_BIGSTUB_DATETIME_FORMAT_2, event_date_string):
            bigstub_event_datetime_format_string = "%b %d, %Y %I:%M %p"
            need_to_add_current_year = False
        else:
            sys.exit("Mistakes were made.")

        if need_to_add_current_year:
            current_year = datetime.date.today().year
            event_datetime_string = "{event_date_string} {current_year} {event_time_string}".format(event_date_string = event_date_string, current_year = current_year, event_time_string = event_time_string)
        else:
            event_datetime_string = "{event_date_string} {event_time_string}".format(event_date_string = event_date_string, event_time_string = event_time_string)
            
        event_datetime = datetime.datetime.strptime(event_datetime_string, bigstub_event_datetime_format_string)
        
        return event_datetime

    def get_event_url_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_url = upcoming_events_list_item.find("div", {"class": "title-holder"}).h3.a['href']
        
        return event_url

    def get_event_id_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_url = upcoming_events_list_item.find("div", {"class": "title-holder"}).h3.a['href']
        
        re_search = re.search(REGEX_UPCOMING_EVENTS_EVENT_ID, event_url)
        
        event_id = re_search.group(1).strip()
        
        return event_id

    def get_event_name_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_name = str(upcoming_events_list_item.find("div", {"class": "title-holder"}).h3.a.contents[0]).strip()
        
        return event_name

    def get_event_venue_name_and_location_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_venue_name_and_location = str(upcoming_events_list_item.find("div", {"class": "title-holder"}).strong.contents[0]).strip()
        
        return event_venue_name_and_location

    def get_event_venue_name_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_venue_name_and_location = str(upcoming_events_list_item.find("div", {"class": "title-holder"}).strong.contents[0]).strip()
        
        event_venue_name = event_venue_name_and_location[::-1].split("-", 1)[1][::-1].strip()
        
        return event_venue_name

    def get_event_venue_location_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_venue_name_and_location = str(upcoming_events_list_item.find("div", {"class": "title-holder"}).strong.contents[0]).strip()
        
        event_venue_location = event_venue_name_and_location[::-1].split("-", 2)[0][::-1].strip()
        
        return event_venue_location

    def get_event_venue_city_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_venue_name_and_location = str(upcoming_events_list_item.find("div", {"class": "title-holder"}).strong.contents[0]).strip()
        
        event_venue_location = event_venue_name_and_location[::-1].split("-", 2)[0][::-1].strip()
        
        event_venue_city = event_venue_location.split(",", 2)[0].strip()
        
        return event_venue_city

    def get_event_venue_state_from_upcoming_events_list_item(self, upcoming_events_list_item):
        
        event_venue_name_and_location = str(upcoming_events_list_item.find("div", {"class": "title-holder"}).strong.contents[0]).strip()
        
        event_venue_location = event_venue_name_and_location[::-1].split("-", 2)[0][::-1].strip()
        
        event_venue_state = event_venue_location.split(",", 2)[1].strip()
        
        return event_venue_state

    def process_upcoming_events_list_items(self):
        
        upcoming_events_list_items = self.get_upcoming_events_list_items()
        #   <class 'bs4.element.ResultSet'>
        
        for upcoming_events_list_item in upcoming_events_list_items:
            
            event_datetime = self.get_event_datetime_from_upcoming_events_list_item(
                upcoming_events_list_item)
    
            event_url = self.get_event_url_from_upcoming_events_list_item(upcoming_events_list_item)
    
            event_id = self.get_event_id_from_upcoming_events_list_item(upcoming_events_list_item)
    
            event_name = self.get_event_name_from_upcoming_events_list_item(
                upcoming_events_list_item)
    
            event_venue_name = self.get_event_venue_name_from_upcoming_events_list_item(
                upcoming_events_list_item)
    
            event_venue_city = self.get_event_venue_city_from_upcoming_events_list_item(
                upcoming_events_list_item)
    
            event_venue_state = self.get_event_venue_state_from_upcoming_events_list_item(
                upcoming_events_list_item)
    
            # #################### #
            # BEGIN: Event Details #
            # #################### #
    
            event_details = list()
            event_details.append(event_datetime)
            event_details.append(event_url)
            event_details.append(event_id)
            event_details.append(event_name)
            event_details.append(event_venue_name)
            event_details.append(event_venue_city)
            event_details.append(event_venue_state)
    
            print("event_details: {}".format(str(event_details)))
    
            big_stub_event = BigStubEvent(event_datetime,
                                          event_url,
                                          event_id,
                                          event_name,
                                          event_venue_name,
                                          event_venue_city,
                                          event_venue_state)
    
            record_ts = datetime.datetime.now()
    
            values = (event_datetime,
                      event_url,
                      event_id,
                      event_name,
                      event_venue_name,
                      event_venue_city,
                      event_venue_state,
                      record_ts)

            # mysql_connection = ats_mysql.get_mysql_connection(configuration)
            # mysql_cursor = ats_mysql.get_mysql_cursor(mysql_connection)
            # mysql_cursor.execute(SQL_INSERT_INTO_BIGSTUB_SCRAPER_CHICAGO_IL_EVENTS, values)

            MysqlConnectionManager.mysql_cursor.execute(SQL_INSERT_INTO_BIGSTUB_SCRAPER_CHICAGO_IL_EVENTS, values)

            # with MysqlConnectionManager.mysql_cursor as mysql_cursor:
            #     mysql_cursor.execute(SQL_INSERT_INTO_BIGSTUB_SCRAPER_CHICAGO_IL_EVENTS, values)

            # #################### #
            # END: Event Details #
            # #################### #
    
            # sys.exit("Le Fin.")
