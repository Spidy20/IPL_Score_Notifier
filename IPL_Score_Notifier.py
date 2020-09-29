import requests
from bs4 import BeautifulSoup
import time
from plyer import notification

while True:
    ## Open the site
    url = "https://www.scorespro.com/rss2/live-cricket.xml"
    r = requests.get(url)
    ## FInd the text from site
    sp = BeautifulSoup(r.text,'html.parser')
    ## FInd the Score related to IPL
    data = sp.find_all('title')
    d = data[2].text
    d = d[32:]
    ## We got the score
    print(d)
    ## Set the notification for windows.
    notification.notify(
    title = "IPL Score Notifier",
    message = str(d),
    app_name='IPL 2020',
    app_icon='ipl.ico',
    timeout = 15
    )
    time.sleep(20)