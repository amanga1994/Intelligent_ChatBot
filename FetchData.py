import csv
import bs4, requests
url ='https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#compsci'

def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")

soup = get_page_contents(url)
data = soup.find_all("a", id="compsci")
actual = data[0].parent.parent
title = list()
uniqueId = list()
description = list()
for x in actual.find_all("b"):
    if x.i and x.i.text != "\n":
        title.append(x.i.text.encode('ascii', 'ignore').decode('ascii'))
        uniqueId.append(x.contents[0].encode('ascii', 'ignore').decode('ascii'))
        description.append(x.next_sibling.next_sibling.next_sibling.encode('ascii', 'ignore').decode('ascii').replace("\n",""))

print(title)
print(uniqueId)
print(description)
print(type(title[0]))

with open("data.csv", "w") as csv_file:
    writer = csv.writer(csv_file,delimiter=",")
    for i in range(0, len(title)):
        s = uniqueId[i]
        # csv_file.write(s)
        writer.writerow((uniqueId[i],title[i],description[i]))
