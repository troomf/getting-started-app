import requests
import xml.etree.ElementTree as ET
import os
import array
#clearapi_key = os.environ['API_KEY']
#file_path = os.environ['FILE_PATH']
from variables import *


categories = ["Movies", "TVShows", "Music", "Games", "Ebooks", "Apps", "Adult"]
for i in categories:
    print(categories.index(i)+1)
    if not os.path.exists(file_path+i):
         os.mkdir(file_path+i)
    url = 'https://milkie.cc/api/v1/rss?categories='+str(categories.index(i)+1)+'&ad.q=1080p&key='+api_key
    print (url)
    response = requests.get(url)
    if response.status_code == 200:
        rss_feed = response.text
        root = ET.fromstring(rss_feed)
        for items in root[0].findall('item'):
            title = items.find('title').text
            link = items.find('link').text
            response = requests.get(link)
            if response.status_code == 200:
                with open(file_path+i+'/'+title+'.torrent', 'wb') as file:
                 file.write(response.content)





