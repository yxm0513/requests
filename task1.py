import requests
from bs4 import BeautifulSoup
import xlwt


title = 'text, title,forename,surname,email 1,email2,email3,tel 1,tel2,tel3,fax1,fax2,fax3,telfax1,telfax2,telfax3,mobile,Reg,Association,Country,City,State,department,Institute,street_no,Street1,Street2,Pobox,website 1,Specialty,gender,URL,language-spoken,handled by,postcode'
#        0     1        2        3       4      5      6      7      8   9   10  11    12   13       14     15      16     17    18        19      20   21     22         23       24           25    26     27   28         29         30   31   32               33       34
#设置表格样式
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
        for k in range(0, len(row0)-1):
            #print(k)
            sheet1.write(j, k, d[k])
        j += 1
    f.save('standard_source template.xls')



base = 'https://www.sccad.net/'
url = 'https://www.sccad.net/directorio-medico-sccad.php'


rsp =  requests.get(url)
soup = BeautifulSoup(rsp.text, 'html.parser')
print(soup.prettify())
url_list = {}

for link in soup.find_all('a'):
    if link.get('href').find('directorio/') != -1:
        if link.get('href') not in url_list:
            url_list[link.get('href')] = link.get_text().strip()

#print(url_list)
all = {}
for k in url_list:
    u = base + k
    rsp = requests.get(u)
    s = BeautifulSoup(rsp.text, 'html.parser')
    #print(s.prettify())
    for link in s.find_all('a'):
        if link.get('href').find('perfil.php?id') != -1:
            if link.get('href') not in all:
                all[link.get('href')] = url_list[k]

data = []
print("total")
print(len(all.keys()))
m = 0
for l in all:
    m += 1
    print(m)
    #if m == 4:
    #    write_excel(data)
    #    exit()
    text = ''
    d = {}
    for i in range(34):
        d[i] = ''
    u =  base + 'directorio/' + l
    rsp = requests.get(u)
    soup = BeautifulSoup(rsp.text, 'html.parser')
    name = soup.find('span',class_="mid")
    text += name.get_text()
    tmp = name.get_text().strip().split(' ')
    if tmp[0].find('Dr') != -1:
        d[1] = tmp[0].strip()
        tmp.pop(0)
    d[2] = tmp[0].strip()
    d[3] = ' '.join(tmp[1:]).strip()
    address = soup.find("address")
    text += address.get_text()
    #
    d[18] = all[l]
    tmp = address.get_text().strip().split('\n')
    #tmp[1].lower().find('centro') != -1  or tmp[0].lower().find('médico') != -1  or
    if tmp[0].lower().find('clínicas') != -1 or tmp[0].lower().find('policlínica') != -1:
        k = tmp[1].split('.')
        if (k[0].lower().find('clínicas') != -1 or k[0].lower().find('policlínica') != -1) and len(k) > 1:
            d[23] = k[0].strip()
            d[25] = '.'.join(k[1:]).strip()
        else:
            k = tmp[1].split(',')
            if (k[0].lower().find('clínicas') != -1 or k[0].lower().find('policlínica') != -1) and len(k) > 1:
                d[23] = k[0].strip()
                d[25] = ','.join(k[1:]).strip()
            else:
                d[25] = tmp[1].strip()
    else:
        k = tmp[1].split(',')
        if (k[0].lower().find('hospital') != -1 or k[0].lower().find('instituto') != -1 or  k[0].lower().find('medica') != -1  or k[0].lower().find('médico') != -1) and len(k) > 1:
            d[23] = k[0].strip()
            d[25] = ','.join(k[1:]).strip()
        else:
            d[25] = tmp[1].strip()

    la = tmp[2].strip().split(',')
    d[20] = la[0] 
    if len(la) > 1:
        d[21] = la[1]
    else:
        print(u)
        print(tmp)
        print(la)
    d[19] = tmp[3].strip()
    d[29] = 'Dermatologia'
    d[31] = u

    link = address.find_all('a')
    indexe = 0
    indext = 0
    for l in link:
        text += l.get('href') + '\n'
        if l.get('href').find('@') != -1:
            d[4 + indexe] = l.get('href').split(':')[1]
            indexe += 1
            continue
        if l.get('href').find('http') != -1:
            d[28] = l.get('href')
    cel = address.find("h5", text="Celular :")
    if cel:
        q = cel.find_next_sibling("a")
        if q.get('href').find('tel:') != -1:
            d[16] = q.get('href').split(':')[1]
    tel = address.find("h5", text="Teléfono :")
    if tel:
        w = tel.find_next_sibling("a")
        if w.get('href').find('tel:') != -1:
            d[7] = w.get('href').split(':')[1]

    #d[0] = text
    data.append(d)


write_excel(data)

# name =   span class="mid"
# Title: Dr.
#
# Forename: Charles E. H.
#
# Surname: McKeever

# Association : Asociación Panameña de Dermatologia

# address
#          <address>
#            <h5>
#             <span>
#              Dirección :
#             </span>
#            </h5>
#            6a. Avenida 9-18 Zona 10, Edificio Sixtino II, Ala I, Clínica 908
#            <br/>
#            Guatemala, Guatemala
#            <br/>
#            Guatemala
#            <br/>
#            <h5>
#             <span>
#              Teléfono :
#             </span>
#            </h5>
#            <a data-ajax="true" href="tel:+50222783134" rel="external">
#             50222783134
#            </a>
#            <br/>
#           </address>
# tel
# href="tel:+50222783134"
# <a href="http://drcharlesmckeever.com/" target="_blank" rel="external" data-ajax="true"> Ir a Sitio Web </a>

# email : <input id="mail" name="mail" type="hidden" value="derma.cirugia@gmail.com"/>

# Specialty
