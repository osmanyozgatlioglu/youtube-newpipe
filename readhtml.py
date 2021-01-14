from bs4 import BeautifulSoup
import json

html=open('/home/osman/python/abc.html','r').read()
soup = BeautifulSoup(html,'lxml')
data  = soup.find_all("script")[28].string
tt=data[data.index('{'):-1]
vv = json.loads(tt)
gg = vv['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['shelfRenderer']['content']['expandedShelfContentsRenderer']['items']

subscriptions=[]

for subdata in gg:
    ch_name=subdata['channelRenderer']['title']['simpleText']
    ch_link=subdata['channelRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    print(f'{ch_name} {ch_link}')
    subscriptions.append({"service_id": 0,"url": "https://www.youtube.com"+ch_link,"name": ch_name})

finalstr={"app_version": "0.20.8","app_version_int": 962, "subscriptions": subscriptions }

target = open("data.json","w")
target.write(json.dumps(finalstr))
