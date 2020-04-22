from bs4 import BeautifulSoup
# from selenium import webdriver
import xlwt, time
import marshal
import gevent.monkey
gevent.monkey.patch_all()
import requests
import grequests
import csv
import json
from openpyxl import Workbook
import base64
#from PDFWriter import PDFWriter

#import pdfkit
import warnings
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
warnings.filterwarnings(action="ignore", module=".*grequests.*")
warnings.filterwarnings(action="ignore", module=".*urllib3.*")


serach = 'https://www.taoguba.com.cn/useful?pageNo=%s&blockID=0&flag=0'

urls = []
for c in range(0, 1862):
    b = serach % c
    urls.append(b)



def my_exception_handler(req, e):
    print(req)
    print(e)
    print(dir(req))
    print(dir(e))

MAX_CONNECTIONS = 50  # Number of connections you want to limit it to
all = []
pages = len(urls)
for i in range(1, pages + 1, MAX_CONNECTIONS):
    print("1 Waiting %s" % i)  # Optional, so you see something is done.
    rs = (grequests.get(u, timeout=1000, verify=False) for u in urls[i:i + MAX_CONNECTIONS])
    a = list(rs)
    time.sleep(0.2)  # You can change this to whatever you see works better.
    results = grequests.map(a, exception_handler=my_exception_handler)  # The key here is to extend, not append, not insert.
    print("result1 : %s" % len(results))
    print(results)
    for x in results:
        if x:
            print(x.status_code)
            try:
                soup = BeautifulSoup(x.text, 'html.parser')

                content = soup.find('div', class_='p_list01')
                content1 = content.find('li',class_='pcdj02')
                if content1:
                    l = content1.find('a')
                    link = l.get('href')
                    print("link" + link)
                    all.append('https://www.taoguba.com.cn/%s' % link)
            except:
                pass
            x.close()
    if i == 1:
        #break
        pass

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

all_html = {}
pages = len(all)
print("total %s"%pages)
print(all)
done_all= []
try:
    done = open("done", 'rb')
    done_all=marshal.load(done)
    done.close()
except:
    pass


for a in all:
    if a in done_all:
        all.remove(a)
    else:
        done_all.append(a)


for i in range(1, pages + 1, MAX_CONNECTIONS):
    print("2 Waiting %s" % i)  # Optional, so you see something is done.
    rs = (grequests.get(u, verify=False, timeout=1000) for u in all[i:i + MAX_CONNECTIONS])
    time.sleep(0.2)  # You can change this to whatever you see works better.
    results = grequests.map(rs, exception_handler=my_exception_handler)  # The key here is to extend, not append, not insert.
    #print("result2 : %s" % len(results))
    for x in results:
        if x:
            #print(x.status_code)
            try:
                soup = BeautifulSoup(x.text, 'html.parser')
                content = soup.find('div',class_='p_coten')
                for img in content.find_all('img'):
                    t = img.attrs['src']
                    if t.find('placeholder') != -1:
                        t = img.attrs['src2'] 
                    img.attrs['src'] = "data:image;base64,%s" % get_as_base64(t).decode("utf-8")
                all_html[x.url] = content.prettify()
            except:
                pass
            x.close()
    if i == 1:
        #break
        pass

done = open("done", 'wb')
marshal.dump(done_all, done)
done.close()


html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
'''
for k in all_html:
    html += k + '<br>' + all_html[k] + '<hr>'

html += "</body></html>"

font_config = FontConfiguration()
css = CSS(string='''
    * {
        font-size : 0.8rem;
    }
    body {
        backgroud: black;
    }
    @font-face {
        font-family: Gentium;
        src: url(http://example.com/fonts/Gentium.otf);
    }
    h1 { font-family: Gentium }
    img {width: 30; height: 60}''', font_config=font_config)

#print(html)
report_html = HTML(string=html)
report_html.write_pdf(target='vote.pdf', stylesheets=[css],
    font_config=font_config)
