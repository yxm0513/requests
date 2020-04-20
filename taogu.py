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

import warnings
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
warnings.filterwarnings(action="ignore", module=".*grequests.*")
warnings.filterwarnings(action="ignore", module=".*urllib3.*")

def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)


x = requests.get('https://www.taoguba.com.cn/Article/2783155/1', verify=False, timeout=1000)

soup = BeautifulSoup(x.text, 'html.parser')
content = soup.find('div',class_='p_coten')
for img in content.find_all('img'):
    t = img.attrs['src']
    if t.find('placeHolder') != -1:
       t = img.attrs['src2'] 
    img.attrs['src'] = "data:image;base64,%s" % get_as_base64(t).decode("utf-8")
    img['width'] = 100
    img['onload'] =''
    #print(img)
h = content.prettify()

html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
'''

html += '<br>' + h + '<hr>'
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
report_html.write_pdf(target='test.pdf', stylesheets=[css],
    font_config=font_config)

