import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
import xlwt, time
import marshal
import grequests
import csv
import re


from openpyxl import Workbook

title = 'title,forename,surname,email 1,email2,email3,email1 origin,email2 origin,email3 origin,tel 1,tel2,tel3,fax1,fax2,fax3,telfax1,' \
        + 'telfax2,telfax3,mobile,Reg,Association,Country,City,State,dept,Institute,street_no,Street1,Street2,Pobox,website 1,Specialty,' \
        + 'gender,URL,language-spoken,handled by,postcode,Domain'


        # 1    2          3      4        5     6      7              8             9            10      11  12   13   14   15    16
        # 17      18       19    20   21          22     23    24    25    26        27       28      29      30     31         32
        # 33    34    35             36          37     38
def write_xlsx(data):
    book = Workbook()
    sheet = book.active
    sheet.append(title.split(','))
    for row in data:
        sheet.append(row)

    book.save('a.xlsx')


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


# 写Excel
def write_excel(data):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('standard source template')
    row0 = title.split(',')
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    j = 1
    for d in data:
        for k in range(0, len(row0) - 1):
            # print(k)
            sheet1.write(j, k, d[k])
        j += 1
    f.save('a.xls')





url = 'https://www.viin.org.au/find-a-member/'
rsp = requests.get(url, verify=False)
soup = BeautifulSoup(rsp.text, 'html.parser')


urls = []
for link in soup.find_all('a'):
    if link.get('href').find('/member/') != -1:
        urls.append('https://www.viin.org.au/'+ link.get('href').strip())

print("一共")
print(len(urls))

def my_exception_handler(req, e):
    print(req)
    print(e)
    print(dir(req))
    print(dir(e))

MAX_CONNECTIONS = 50  # Number of connections you want to limit it to

content = {}
# pages = len(urls)
# for i in range(1, pages + 1, MAX_CONNECTIONS):
#     print("1 Waiting %s" % i)  # Optional, so you see something is done.
#     rs = (grequests.get(u, timeout=100, verify=False) for u in urls[i:i + MAX_CONNECTIONS])
#     time.sleep(0.2)  # You can change this to whatever you see works better.
#     results = grequests.map(rs, exception_handler=my_exception_handler)  # The key here is to extend, not append, not insert.
#     print("result : %s" % len(results))
#     for x in results:
#         if x:
#             print(x.status_code)
#             try:
#                 content[x.url] = x.text
#             except:
#                 pass
#             x.close()
#     if i == 1:
#         #break
#         pass
#
# soup_file = open("all_html8", 'wb')
# marshal.dump(content, soup_file)
# soup_file.close()

soup_file = open("all_html8", 'rb')
content=marshal.load(soup_file)
soup_file.close()

allsoup = []
all = []

data = []
print('haha')
print(len(content.keys()))
for c in content:
    d = []
    for i in range(38):
        d.append('')
    soup = BeautifulSoup(content[c], 'html.parser')
    m = soup.find('div', class_='member-info')
    x = m.find('h2').get_text().strip()
    tmp = x.split(' ')
    # title
    if len(tmp) >= 3:
        d[0] = tmp[0]
        d[1] = tmp[1]
        d[2] = tmp[2]
    else:
        d[0] = tmp[0]
        d[1] = tmp[1]

    y = m.find('p').get_text().strip()
    d[25] = y.split('\n')[2]
    d[24] = y.split('\n')[1]

    d[33] = c
    d[20] = 'Victorian Infection and Immunity Network'
    d[31] = 'Infectious diseases and Immunology'

    if m.find('a'):
        e = m.find('a',href=re.compile(r"^mailto:")).get_text().strip()
        d[3] = e

    data.append(d)

write_xlsx(data)

