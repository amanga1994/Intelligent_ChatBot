import csv
import bs4, requests

list_Id = list()
title = list()
uniqueId = list()
description = list()
urls = list()

list_Id = ['actuarial', 'courses', 'classics', 'arabic', 'chinese', 'german', 'italian', 'spanish0', 'Linguistics',
           'modernlang', 'sexuality',
           'womens-studies', 'Geography', 'Geology', 'cata', 'Francais_langue_seconde', 'education', 'library_studies',
           'BSTA', 'BTM',
           'SCOM', 'b61.35,''compsci', 'softeng', 'b81.30', 'filmstud''comparts', 'designart', 'electro', 'jazz',
           'jazzhist', 'jazzperf', 'mushist', 'musperf', 'music', 'filmstud', 'courses']


# list_Id = ['courses','filmstud']

url = 'https://www.concordia.ca/academics/undergraduate/calendar/current/sec71/71-70.html#compsci'


def read_and_parse_urls():
    global data_set
    data_set = {}
    f = open("final_course_links.txt", "r")
    urls = f.readlines()
    for url in urls:
        course_info = extract_course_info(url.strip())


#         if course_info is not None:
#             data_set.append(course_info.copy())

def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return bs4.BeautifulSoup(page.text, "html.parser")


def extract_course_info(url):
    soup = get_page_contents(url)
    global list_id
    for id in list_Id:
        data = soup.find_all("a", id=id)
        if len(data) > 0:
            actual = data[0].parent.parent
        else:
            continue

        global title
        global uniqueId
        global description
        global urls
        for x in actual.find_all("b"):
            if x.i and x.i.text != "\n" and type(x.contents[0]) is bs4.element.NavigableString and type(
                    x.next_sibling.next_sibling.next_sibling) is bs4.element.NavigableString and (
            x.contents[0].encode('ascii', 'ignore').decode('ascii')).strip() not in uniqueId and len(
                    x.i.text.encode('ascii', 'ignore').decode('ascii')) > 0 and len(
                    x.next_sibling.next_sibling.next_sibling.encode('ascii', 'ignore').decode('ascii').replace("\n",
                                                                                                               "")) > 0:
                print(type(x.contents[0]))
                title.append(x.i.text.encode('ascii', 'ignore').decode('ascii'))
                uniqueId.append(x.contents[0].encode('ascii', 'ignore').decode('ascii').strip())
                description.append(
                    x.next_sibling.next_sibling.next_sibling.encode('ascii', 'ignore').decode('ascii').replace("\n",
                                                                                                               ""))
                urls.append(url)


def write_into_file():
    with open("data.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        for i in range(0, len(title)):
            s = uniqueId[i]
            # csv_file.write(s)
            writer.writerow((uniqueId[i], title[i], description[i], urls[i]))


read_and_parse_urls()
write_into_file()