import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
import xlwt, time
import marshal
#import gevent.monkey
#gevent.monkey.patch_all()
import grequests
import csv
import json
from openpyxl import Workbook
import warnings

warnings.filterwarnings(action="ignore", module=".*grequests.*")
warnings.filterwarnings(action="ignore", module=".*urllib3.*")
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


code = '''
512
1
2
3
513
7
507
489
486
468
88
514
112
129
609
130
515
135
158
516
586
170
626
587
177
592
655
360
593
222
517
635
384
230
620
246
595
532
248
262
643
296
304
330
334
553
619
348
533
366
367
368
373
534
601
383
354
596
395
411
634
610
550
420
428
429
633
627
432
505
506
463
'''

base = 'https://www.pennmedicine.org/providers?searchby=name&uispecialtyid=%s&fadf=PennMedicine'

allsoup = []
all = []

data = []
m = 1

urls = []
for c in code.split('\n'):
    if c:
        # print(m)
        m += 1
        b = base % c
        # print(b + '\n')
        urls.append(b)

def my_exception_handler(req, e):
    print(req)
    print(e)
    print(dir(req))
    print(dir(e))

MAX_CONNECTIONS = 50  # Number of connections you want to limit it to
print(1111111)
pages = len(urls)
for i in range(1, pages + 1, MAX_CONNECTIONS):
    print("1 Waiting %s" % i)  # Optional, so you see something is done.
    rs = (grequests.get(u, timeout=100, verify=False) for u in urls[i:i + MAX_CONNECTIONS])
    a = list(rs)
    time.sleep(0.2)  # You can change this to whatever you see works better.
    results = grequests.map(a, exception_handler=my_exception_handler)  # The key here is to extend, not append, not insert.
    print("result1 : %s" % len(results))
    for x in results:
        if x:
            print(x.status_code)
            try:
                soup = BeautifulSoup(x.text, 'html.parser')
                for link in soup.find_all('a'):
                    if link.get('href'):
                        if link.get('href').find('/providers/profile/') != -1:
                            if link.get('href') not in all:
                                all.append( 'https://www.pennmedicine.org' + link.get('href'))
            except:
                pass
            x.close()
    if i == 1:
        # break
        pass

print(2222222)
all_html = {}
pages = len(all)
for i in range(1, pages + 1, MAX_CONNECTIONS):
    print("2 Waiting %s" % i)  # Optional, so you see something is done.
    rs = (grequests.get(u, verify=False, timeout=1000) for u in all[i:i + MAX_CONNECTIONS])
    time.sleep(0.2)  # You can change this to whatever you see works better.
    results = grequests.map(rs, exception_handler=my_exception_handler)  # The key here is to extend, not append, not insert.
    print("result2 : %s" % len(results))
    for x in results:
        if x:
            print(x.status_code)
            try:
                all_html[x.url] = x.text
            except:
                pass
            x.close()
    if i == 1:
        # break
        pass


soup_file = open("all_html5", 'wb')
marshal.dump(all_html, soup_file)
soup_file.close()
#
# soup_file = open("all_html5", 'rb')
# all_html=marshal.load(soup_file)
# soup_file.close()

print(333333)
for key in all_html:
    soup = BeautifulSoup(all_html[key], 'html.parser')

    d = []
    for i in range(38):
        d.append('')
    # t = soup.find("div", class_="fad-provider-bio__title-matin")
    # if t:
    #     x = t.get_text().strip().split(',')
    #     d[1] = x[0].split(' ')[0]
    #     d[2] = x[0].split(' ')[1]
    #     d[0] = ' '.join(x[1:])
    # else:
    #     print(" 1 " + soup.get_text().strip())
    # t = soup.find("div", class_="fad - listing__list - item - title - main")
    # if t:
    #     x =  t.get_text().strip().split(',')
    #     d[26] = x
    # else:
    #     print(" 2 " + soup.get_text().strip())
    # t = soup.findAll("div", class_="fad - listing__list - item - address - title")
    # if t:
    #     p[10] = t[-1].get_text().strip()
    #
    #     t = t[-2].get_text().strip().spilt(',')
    #     d[22] = t[0]
    #     g = t[1].split(' ')
    #     d[23] = g[0]
    #     d[36] = g[1]
    #     d[27] = ' '.join(t[:-2])
    # else:
    #     print(" 3 " + soup.get_text().strip())
    # t = soup.find("div", class_="fad - provider - bio__ul fad - provider - bio__ul - -lg")
    # if t:
    #     d[34] = t.get_text().strip()
    # d[30] = key
    h = json.loads(soup.find('script', type='application/ld+json').text)
    x = h['name']
    if x:
        #print(x)
        d[1] = x.split(',')[0].split(' ')[0]
        d[2] = x.split(',')[0].split(' ')[1]
        d[0] = ','.join(x.split(',')[1:])
    #print(h['address'])
    if h['address']:
        try:
            y = h['address'][0].split(',')
            d[25] = y[0]
            d[27] = ' '.join(y[1:-3])
            d[36] = y[-1]
            d[22] = y[-3]
            d[23] = y[-2]
        except:
            y = h['address'].split(',')
            d[25] = y[0]
            d[27] = ' '.join(y[1:-3])
            d[36] = y[-1]
            d[22] = y[-3]
            d[23] = y[-2]
    d[30] =h['url']
    d[9] = h['telephone']
    if h['medicalSpecialty']:
        d[31] = ','.join(h['medicalSpecialty'])
    if not h['medicalSpecialty'] and h['department']:
        d[31] = ','.join(h['department'])

    data.append(d)
    m += 1
    if m == 3:
        pass
        #break

write_xlsx(data)
