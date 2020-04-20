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



content= ''

with open('a.html', 'r+',encoding='ISO-8859-1') as f:
    content = f.read()

soup_file = open("all_html6", 'wb')
marshal.dump(content, soup_file)
soup_file.close()

soup_file = open("all_html6", 'rb')
content=marshal.load(soup_file)
soup_file.close()

allsoup = []
all = []

data = []
m = 1

soup = BeautifulSoup(content, 'html.parser')


for t in soup.findAll('table'):
    x = t.get_text().strip()
    if x:
        print('-' * 60)
        #print(x)

        tr = t.findAll('tr')
        if tr:
            d = []
            for i in range(38):
                d.append('')
            try:
                d[0], d[1], d[2] = tr[1].get_text().split(' ')
            except:
                print(t.get_text())

            for h in tr:
                if h.get_text().strip().find('Bureau') != -1:
                    for y in h.get_text().strip().split('-'):
                        if y.find('Bureau') != -1:
                            d[9] = y.split(':')[1]
                        if y.find('Portable') != -1:
                            d[18] = y.split(':')[1]
                        if y.find('Fax') != -1:
                            d[12] = y.split(':')[1]
                if h.get_text().strip().find('FRANCE') != -1:
                    print(h.get_text())
                    l = re.search("(\d{5})", h.get_text())
                    if l:
                        p = re.compile("(\d{5})").split(h.get_text())
                        d[27] = p[0]
                        d[36] = p[1]
                        d[21] = 'FRANCE'
                        d[22] = p[2].split('(')[0]
                    else:
                        d[21] = 'FRANCE'
                        d[27] = h.get_text().split('(')[0]

                if h.get_text().strip().find('E-mail') != -1:
                    tmp = h.get_text().split('\n')
                    for k in tmp:
                        if k.find('E-mail') != -1:
                            d[3] =  k.split(':')[1]
            if tr[2].get_text():
                d[31] = tr[2].get_text().strip()
            d[33] = 'ff2p.fr'
            data.append(d)

write_xlsx(data)

'''

'''