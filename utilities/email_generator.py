from datetime import datetime


def email_timestamp_generator():
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "chetan" + timestamp + "@gmail.com"

