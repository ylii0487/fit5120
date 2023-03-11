import datetime

import view
import database

page_view = view.View()
database = database.MySQLDatabase()

database.tables_setup()

def home_page():
    return page_view("HomePage")


def classification_page():
    return page_view("Classification")


def trend_page():
    return page_view("WasteMap")


def event_page():
    return page_view("Event")


def create_eventPage():
    return page_view("createEvent")


def create_event(event_topic, event_time, event_place, contact_details, event_content):
    if event_topic is None or event_time is None or event_place is None or event_content is None or contact_details:

        err_str = "Username or Password or Role or Email cannot be null"

        return page_view("invalid_add", reason=err_str)

    else:

        event_create = database.add_event(event_topic, event_time, event_place, contact_details, event_content)


        if event_create:
            return page_view("Event")
        else:
            err_str = "The new event is duplicate"
            return page_view("invalid_add", reason=err_str)


def feedback_page():
    return page_view("Feedback")


def faq_page():
    return page_view("FAQ")


def about_page():
    return page_view("AboutUs")
