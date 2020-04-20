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


#
# content= ''
#
# with open('7.html', 'r+') as f:
#     content = f.read()
#
# soup = BeautifulSoup(content, 'html.parser')
#
# urlkey = []
# o = soup.findAll('option')
# for i in o:
#     urlkey.append(i['value'])
#
# base = 'https://cpspei.ca/public-info/physician-search-2/?lastname=&firstname=&specialty=%s&searchsubmit=Search'
#
# urls = []
# for key in urlkey:
#     u = base % key
#     urls.append(u)
#
#
# def my_exception_handler(req, e):
#     print(req)
#     print(e)
#     print(dir(req))
#     print(dir(e))
#
# MAX_CONNECTIONS = 50  # Number of connections you want to limit it to
#
# content = {}
# pages = len(urls)
# for i in range(1, pages + 1, MAX_CONNECTIONS):
#     print("1 Waiting %s" % i)  # Optional, so you see something is done.
#     rs = (grequests.get(u, timeout=100, verify=False) for u in urls[i:i + MAX_CONNECTIONS])
#     time.sleep(0.2)  # You can change this to whatever you see works better.
#     results = grequests.map(rs, exception_handler=my_exception_handler)  # The key here is to extend, not append, not insert.
#     print("result1 : %s" % len(results))
#     for x in results:
#         if x:
#             print(x.status_code)
#             try:
#                 content[x.url] = x.text
#             except:
#                 pass
#             x.close()
#     if i == 1:
#         # break
#         pass
#
# soup_file = open("all_html7", 'wb')
# marshal.dump(content, soup_file)
# soup_file.close()

soup_file = open("all_html7", 'rb')
content=marshal.load(soup_file)
soup_file.close()

allsoup = []
all = []

data = []
m = 1

for c in content:
    soup = BeautifulSoup(content[c], 'html.parser')
    s = soup.find('option', {'selected': True}).get_text().strip()

    for t in soup.find_all('div', class_='row'):
        d = []
        for i in range(38):
            d.append('')
        d[33] = c
        d[31] = s
        if t:
            print('-' * 80)
            print(t.get_text().strip())
            w1 = t.find('div',class_='w1')
            if w1:
                x = w1.get_text().strip()
                tmp1 = x.split(',')
                d[1] = tmp1[1]
                d[2] = tmp1[0]
            w2 = t.find('div', class_='w2')
            if w2:
                y = w2.get_text().strip()
                tmp2 = y.split('\n')
                print(c)
                if len(tmp2) >= 3:
                    l = ' '.join(tmp2[2].split()).split()
                    try:
                        d[36] = l[-2] + " " + l[-1]
                        d[23] = l[-3]
                        d[22] = l[-4]
                        d[27] = tmp2[1]
                        d[25] = tmp2[0]
                    except:
                        try:
                            d[36] = l[-1]
                            d[23] = l[-2]
                            d[22] = l[-3]
                            d[27] = tmp2[1]
                            d[25] = tmp2[0]
                        except:
                            d[23] = l[-1]
                            d[22] = l[-2]
                            d[27] = tmp2[1]
                            d[25] = tmp2[0]
                else:
                    d[25] = tmp2[0]
            w3 = t.find('div', class_='w3')
            if w3:
                z = w3.get_text().strip()
                d[9] = z
            w4 = t.find('div', class_='w4')

            if w4:
                w = w4.get_text().strip()
                d[15] = w
            w5 = t.find('div', class_='w5')

            if w5:
                q = w5.get_text().strip()
                d[0] = q
            data.append(d)

write_xlsx(data)

