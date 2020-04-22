import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.concordia.ca/academics/undergraduate/calendar/current/courses-quick-links.html")
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify)
f = open("course_links.txt", "w")
for link in soup.findAll('a'):
    url_string = (link.get('href'))
    if(url_string):
        if(len(url_string) >= 24 and ('sec'in url_string)):
            if(url_string[0:24] == '/academics/undergraduate'):
                head, sep, tail = url_string.partition('#')
                f.write('https://www.concordia.ca/' + head + '\n')
f.close()

lines_seen = set()
with open("final_course_links", "w") as output_file:
    for line in open("course_links.txt", "r"):
        if line not in lines_seen:
            output_file.write(line)
            lines_seen.add(line)
