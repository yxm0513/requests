import requests
from bs4 import BeautifulSoup
#from selenium import webdriver
import xlwt, time
import marshal, grequests


title = 'title,forename,surname,email 1,email2,email3,email1 origin,email2 origin,email3 origin,tel 1,tel2,tel3,fax1,fax2,fax3,telfax1,telfax2,telfax3,mobile,Reg,Association,Country,City,State,dept,Institute,street_no,Street1,Street2,Pobox,website 1,Specialty,gender,URL,language-spoken,handled by,postcode,Domain, Appointment'
        # 1    2          3      4        5     6      7              8             9            10      11  12   13   14   15    16     17      18       19   20  21          22     23
  # 24   25    26        27       28      29    30     31         32        33    34    35             36          37     38
def set_style(name,height,bold=False):
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height
	style.font = font
	return style

#写Excel
def write_excel(data):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('standard source template')
    row0 = title.split(',')
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])
    j = 1
    for d in data:
        for k in range(0, len(row0)):
            print(k)
            print(d[k])
            sheet1.write(j, k, d[k])
        j += 1
    f.save('standard_source template.xls')



#wd = webdriver.Chrome()
#base = 'https://iris.ucl.ac.uk/iris/search'
#wd.get(base)


#select = Select(wd.find_element_by_id('meta_x_phrase_sand'))
#select.select_by_visible_text('Researchers')
#wd.find_element_by_id('btnMainAdvSearch').click()
#sleep(30);

base = 'https://iris.ucl.ac.uk/iris/search/funnelbackResults?query=&collection=iris-meta&form=results&meta_x_phrase_sand=iris-researchers&f.Result+Categories%7cx=%2ciris+researchers&start_rank={}&query_and=&query_phrase=&query_not=&meta_t=&meta_O=&meta_d1day=&meta_d1month=&meta_d1year=&meta_d2day=&meta_d2month=&meta_d2year=&meta_N=&meta_S=&sort='
b = 'https://iris.ucl.ac.uk/iris/browse/profile?'
#


all = []
url_list = []
'''
for i in range(9585):
    if i % 10 == 1:
        all.append(base.format(i))

#marshal.dump(all, 'all')

#[:2]
for u in all:
    rsp = requests.get(u, verify=False)
    soup = BeautifulSoup(rsp.text, 'html.parser')
    for link in soup.find_all('a'):
        if link.get('href').find('upi=') != -1:
            if link.get('href') not in url_list:
                url_list.append(link.get('href').split('?')[1])
url_file = open("url_list", 'wb')
marshal.dump(url_list, url_file)
url_file.close()
'''
url_file = open("url_list", 'rb')
url_list=marshal.load(url_file)
url_file.close()



print(url_list)

data = []
print("total")
print(len(url_list))
m =0

all_soup = {}
#url_list=['upi=NPASH45']
urls = []
for l in url_list:
    print(m)
    #if m == 10:
    #   write_excel(data)
    #  exit()
    m += 1
    text = ''
    d = []
    for i in range(39):
        d.append('')
    u =  b + l
    urls.append(u)

MAX_CONNECTIONS = 50  # Number of connections you want to limit it to

content = {}
pages = len(urls)
for i in range(1, pages + 1, MAX_CONNECTIONS):
    print("1 Waiting %s" % i)  # Optional, so you see something is done.
    rs = (grequests.get(u, timeout=100, verify=False) for u in urls[i:i + MAX_CONNECTIONS])
    time.sleep(0.2)  # You can change this to whatever you see works better.
    results = grequests.map(rs)  # The key here is to extend, not append, not insert.
    print("result1 : %s" % len(results))
    for x in results:
        if x:
            print(x.status_code)
            try:
                all_soup[x.url] = x.text
                #all_soup.append(x.text)
            except:
                pass
            x.close()
    if i == 1:
        #break
        pass



soup_file = open("all_soup", 'wb')
marshal.dump(all_soup, soup_file)
soup_file.close()

soup_file = open("all_soup", 'rb')
all_soup=marshal.load(soup_file)
soup_file.close()

for k in all_soup:
    d = []
    for i in range(39):
        d.append('')
    soup = BeautifulSoup(all_soup[k], 'html.parser')
    try:
        name = soup.find("div", class_="displayName").get_text().strip()
        tmp = name.split(' ')
        print(name)
        # title
        if len(tmp) >= 3:
            d[0] = tmp[0]
            d[1] = tmp[1]
            d[2] = tmp[2]
        else:
            d[0] = tmp[0]
            d[1] = tmp[1]
    except:
        print("FAIL " + k + ' displayName\n')
    if not d[1]:
        continue
    try:
        address = soup.find("div", class_="infoAddress").get_text().strip()
        tmp = address.split('\n')
        if len(tmp) == 1:
            d[22] = tmp[0]
        else:
            s = []
            for t in tmp:
                if t.find('London') != -1:
                    d[22] = 'London'
                elif t.find('WC') != -1 or t.find('NW') != -1:
                    d[36] = t
                elif t.find('UK') != -1 or t.find('United Kingdom') != -1:
                    d[21] = t
                elif t.find('Institute') != -1 or t.find('Hospital')  != -1  or t.find('University')  != -1 or   t.find('School')  != -1 or  t.find('Centre')  != -1 :
                    d[25] = t
                elif t.find('Department') != -1 or t.find('Dept') != -1:
                    d[24] = t
                else:
                    s.append(t)
            d[26] = '\n'.join(s)

    except:
        print("FAIL " + k + ' infoAddress\n')
    try:
        infoContact = soup.find("div", class_="infoContact")
        link = infoContact.find_all('a')
        for l in link:
            if l.get('href').find('@') != -1:
                d[3] = l.get('href').split(':')[1]
        div = infoContact.find_all('div')
        for c in div:
            if c.get_text().find('Tel') != -1:
                d[9] = c.get_text().strip().split(":")[1]
    except:
        print("FAIL " + k + ' infoContact\n')
    try:
        webPage = soup.find("div", class_="webPage").get_text().strip()
        d[30] = webPage
    except:
        pass
    try:
        info = soup.find("div", text="Research Themes").parent
        li = info.find_all('li')
        x = []
        for l in li:
          x.append(l.get_text().strip())
        d[31] = ';'.join(x)
    except:
        pass
    try:
        infoContact = soup.find("div", class_="basicInfoLeftRight")
        li = infoContact.find_all('li')
        a = []
        for l in li:
            if l.get_text().find('Research') != -1:
                a.append(l.get_text())
        d[38] = ";".join(a)
        if not d[38]:
            d[38] = li[0].get_text()

    except:
        print("FAIL " + k + ' basicInfoLeftRight\n')

    d[33] = k
    data.append(d)


write_excel(data)
