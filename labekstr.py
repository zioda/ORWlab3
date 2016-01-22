import requests
from bs4 import BeautifulSoup


url = "http://www.trivago.pl/?iPathId=86491&iGeoDistanceItem=0&aDateRange%5Barr%5D=2016-02-07&aDateRange%5Bdep%5D=2016-02-08&iRoomType=7&cpt=8649103&iViewType=0&isRetina=false&bIsSeoPage=false&bIsSitemap=false&"
r = requests.get(url)

soup = BeautifulSoup(r.content)

#links = soup.find_all("a")

#for link in links:
   #  print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("span", {"class": "item_name"})

for item in g_data:
    print item.contents
    
