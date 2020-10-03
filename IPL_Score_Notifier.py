import requests
from bs4 import BeautifulSoup
import time
from plyer import notification

# initial state 0
init = 0
while True:
    # Open the site

    dprev = ""
    url = "https://www.scorespro.com/rss2/live-cricket.xml"
    r = requests.get(url)
    # FInd the text from site
    sp = BeautifulSoup(r.text, 'html.parser')
    # FInd the Score related to IPL
    data = sp.find_all('title')
    d = data[2].text
    d = d[32:]
    # We got the score
    print(d)
    # Set the notification for windows.
    # show score only when it gets changed, if score doesnt change in given sleep time, don't notify
    # gives user realtime ball by ball score update
    if init == 0 or d != dprev:
        notification.notify(
            title="IPL Score Notifier",
            message=str(d),
            app_name='IPL 2020',
            app_icon='ipl.ico',
            timeout=15
        )
    init = 1  # change state to 1
    dprev = d
    time.sleep(10)  # check every 10 seconds to save some banddwidth
