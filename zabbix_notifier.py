from json import dumps
from httplib2 import Http
from credential import WEBHOOK_URL
import sys

def main():
    """Google Chat incoming webhook quickstart."""
    url = WEBHOOK_URL
    eventDate = sys.argv[1]
    eventTime = sys.argv[2]
    hostName = sys.argv[3]
    eventName = sys.argv[4]
    appMessage = {
        "text": 
"""
[test]
Accidents Happening Now.
\n
Datetime : {date} {time}
\n
Host Name : {host}
\n
Accident detail : {detail}
""".format(date = eventDate,
                   time = eventTime,
                   host = hostName,
                   detail = eventName,
                   )}
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(appMessage),
    )

if __name__ == "__main__":
    main()