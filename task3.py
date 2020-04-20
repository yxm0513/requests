import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import xlwt, time
import marshal
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

title = 'title,forename,surname,email 1,email2,email3,email1 origin,email2 origin,email3 origin,tel 1,tel2,tel3,fax1,fax2,fax3,telfax1,telfax2,telfax3,mobile,Reg,Association,Country,City,State,dept,Institute,street_no,Street1,Street2,Pobox,website 1,Specialty,gender,URL,language-spoken,handled by,postcode,Domain'
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
        for k in range(0, len(row0)-1):
            #print(k)
            sheet1.write(j, k, d[k])
        j += 1
    f.save('standard_source template.xls')





#driver = webdriver.Chrome()
base = 'https://www.veniceregional.com/find-a-doctor'
b = 'https://www.veniceregional.com'
#driver.get(base)
page = []
all = []

all_soup=[]

link = ['/find-a-doctor/feinsilber-doron-md-108825', '/find-a-doctor/greenberg-adam-md-17111', '/find-a-doctor/lomas-gregory-md-12486', '/find-a-doctor/dreier-jonathan-md-19449', '/find-a-doctor/jacob-blessy-md-6887', '/find-a-doctor/ulitsky-olga-md-3049', '/find-a-doctor/bancroft-laura-md-135489', '/find-a-doctor/maun-noel-md-11604', '/find-a-doctor/walsh-christopher-md-37240', '/find-a-doctor/charron-albert-md-45168', '/find-a-doctor/silverstein-jeffrey-md-134418', '/find-a-doctor/stelton-christina-md-44277', '/find-a-doctor/pflug-vincent-do-8398', '/find-a-doctor/selva-sergio-md-5632', '/find-a-doctor/willkomm-christopher-md-1865', '/find-a-doctor/moor-john-md-135080', '/find-a-doctor/jaquith-michael-md-14945', '/find-a-doctor/jivitski-andrej-md-26809', '/find-a-doctor/marrero-sandra-md-137500', '/find-a-doctor/nair-alka-md-10126', '/find-a-doctor/taylor-caren-md-125316', '/find-a-doctor/june-emily-md-14519', '/find-a-doctor/devar-nagarajan-md-19813', '/find-a-doctor/barber-laura-md-23764', '/find-a-doctor/greenberg-stuart-md-17099', '/find-a-doctor/patel-bhavin-md-137489', '/find-a-doctor/caballero-carlos-md-22072', '/find-a-doctor/gonzalez-julio-md-17343', '/find-a-doctor/kirkpatrick-dan-md-13777', '/find-a-doctor/diamond-richard-md-19750', '/find-a-doctor/mehserle-william-md-11146', '/find-a-doctor/vihlen-eric-md-2709', '/find-a-doctor/vasile-tracy-do-105683', '/find-a-doctor/kondapalli-ravi-md-13595', '/find-a-doctor/robertie-paul-md-6999', '/find-a-doctor/sallapudi-neetha-md-6224', '/find-a-doctor/caradonna-stephanie-md-21880', '/find-a-doctor/heller-robert-md-16112', '/find-a-doctor/knapp-james-md-13697', '/find-a-doctor/capote-natalia-md-108637', '/find-a-doctor/lifton-robin-md-12686', '/find-a-doctor/hawke-jess-do-16238', '/find-a-doctor/kukula-christina-do-13380', '/find-a-doctor/patrice-stephen-md-8704', '/find-a-doctor/sharma-om-md-5403', '/find-a-doctor/palmire-vincent-md-9076', '/find-a-doctor/wasserman-justin-md-2356', '/find-a-doctor/graham-jemaar-dpm-134877', '/find-a-doctor/abernathy-george-md-25198', '/find-a-doctor/ashby-coeurlida-md-125686', '/find-a-doctor/chebli-joseph-md-21417', '/find-a-doctor/fedako-catherine-md-18661', '/find-a-doctor/davis-cynthia-md-120673', '/find-a-doctor/larabee-heather-md-13114', '/find-a-doctor/roberts-shannon-md-6980', '/find-a-doctor/giblin-kevin-md-17603', '/find-a-doctor/cassidy-john-md-21700', '/find-a-doctor/khan-tariq-md-13963', '/find-a-doctor/rubin-alec-md-6467', '/find-a-doctor/curl-cynthia-do-20448', '/find-a-doctor/shroyer-lindsay-md-135815', '/find-a-doctor/stewart-charles-md-134111', '/find-a-doctor/whisnant-richard-md-2103', '/find-a-doctor/rainer-laura-md-7675', '/find-a-doctor/burk-emily-do-133972', '/find-a-doctor/flavin-kathryn-md-135961', '/find-a-doctor/piotrowski-rebecca-do-8234', '/find-a-doctor/cortman-christopher-psyd-37574', '/find-a-doctor/demasi-ronald-md-19934', '/find-a-doctor/houston-richard-do-135615', '/find-a-doctor/dubin-robert-md-19420', '/find-a-doctor/durrett-scott-md-19307', '/find-a-doctor/millares-avelino-md-10913', '/find-a-doctor/devine-john-md-34699', '/find-a-doctor/carter-travis-md-130094', '/find-a-doctor/mckinney-trenity-md-11277', '/find-a-doctor/mesghali-sheeba-md-11028', '/find-a-doctor/gerhart-corinne-do-118790', '/find-a-doctor/mathew-dilip-md-11652', '/find-a-doctor/jacob-john-md-270', '/find-a-doctor/savov-jordan-md-5996', '/find-a-doctor/swor-gray-md-3886', '/find-a-doctor/basnight-michael-md-23617', '/find-a-doctor/agnello-katie-md-324', '/find-a-doctor/cuff-derek-md-20484', '/find-a-doctor/junagadhwalla-mehanz-md-14520', '/find-a-doctor/true-jeffrey-md-134304', '/find-a-doctor/rodgers-james-do-6882', '/find-a-doctor/hyder-rishad-md-121358', '/find-a-doctor/overbeck-cara-dds-9210', '/find-a-doctor/ruzek-kimberly-md-37481', '/find-a-doctor/job-lindsey-md-100283', '/find-a-doctor/schmidt-brian-do-135387', '/find-a-doctor/suleskey-charles-dpm-4023', '/find-a-doctor/pankhaniya-rohit-md-9034', '/find-a-doctor/mihm-phillip-md-10948', '/find-a-doctor/woolverton-william-md-1640', '/find-a-doctor/widmyer-david-do-36913', '/find-a-doctor/rice-david-md-7174', '/find-a-doctor/chan-david-md-34103', '/find-a-doctor/cook-andrew-g-md-125890', '/find-a-doctor/dave-deven-md-20241', '/find-a-doctor/bolanos-michael-md-135509', '/find-a-doctor/de-leon-ramon-md-20088', '/find-a-doctor/gutierrez-liliana-md-16814', '/find-a-doctor/johnson-keith-md-14763', '/find-a-doctor/maule-cynthia-md-11605', '/find-a-doctor/cantero-julio-md-21910', '/find-a-doctor/wolpmann-michael-md-1711', '/find-a-doctor/bermudez-edmund-md-23273', '/find-a-doctor/geeryan-lisa-md-44212', '/find-a-doctor/miller-kevin-md-10863', '/find-a-doctor/smith-bryan-md-4833', '/find-a-doctor/crouch-fred-md-20529', '/find-a-doctor/napoliello-david-md-10087', '/find-a-doctor/sollot-stephen-do-4619', '/find-a-doctor/ervin-thomas-md-18933', '/find-a-doctor/sylvester-john-md-3873', '/find-a-doctor/weekes-annmarie-do-2273', '/find-a-doctor/tanyous-walid-md-45154', '/find-a-doctor/baga-john-md-23983', '/find-a-doctor/cogburn-william-md-21001', '/find-a-doctor/barre-julie-g-md-109966', '/find-a-doctor/whapshare-gavin-do-461', '/find-a-doctor/morrison-langdon-md-10447', '/find-a-doctor/patete-michael-md-8723', '/find-a-doctor/yeh-joseph-md-1516', '/find-a-doctor/halaby-issam-md-16687', '/find-a-doctor/vicars-holly-do-70580', '/find-a-doctor/aneja-lalit-md-45851', '/find-a-doctor/wright-gary-md-1612', '/find-a-doctor/gomerocure-wadi-md-489', '/find-a-doctor/oberoi-megha-md-115276', '/find-a-doctor/patel-jignesh-md-134307', '/find-a-doctor/scheer-steven-md-5917', '/find-a-doctor/levy-marc-md-12764', '/find-a-doctor/ng-tracy-do-9861', '/find-a-doctor/dawoodjee-yousuf-md-20124', '/find-a-doctor/gonter-paul-md-17357', '/find-a-doctor/van-passel-leonie-md-2927', '/find-a-doctor/blain-timothy-md-23029', '/find-a-doctor/ditrapani-stephenson-tonya-md-19640', '/find-a-doctor/gordon-charles-md-17290', '/find-a-doctor/hassler-ki-do-16275', '/find-a-doctor/depinto-mario-md-19883', '/find-a-doctor/adams-glenn-md-25098', '/find-a-doctor/wei-michael-md-2260', '/find-a-doctor/blood-jeffrey-md-22965', '/find-a-doctor/liquete-egbert-md-133920', '/find-a-doctor/moretta-antonio-md-130087', '/find-a-doctor/phifer-william-md-8364', '/find-a-doctor/pothiwala-pooja-md-8040', '/find-a-doctor/garcia-ruben-md-37461', '/find-a-doctor/reiheld-craig-md-7305', '/find-a-doctor/rodriguez-charles-md-6869', '/find-a-doctor/giannone-louis-dpm-17612', '/find-a-doctor/mater-simone-md-11659', '/find-a-doctor/roggow-brielle-dpm-105685', '/find-a-doctor/protigal-melissa-md-7881', '/find-a-doctor/fezza-john-md-18549', '/find-a-doctor/lin-jack-md-70589', '/find-a-doctor/mathieson-mark-md-133073', '/find-a-doctor/niffenegger-john-md-9773', '/find-a-doctor/shoemaker-steven-md-5222', '/find-a-doctor/vass-suzanna-do-2847', '/find-a-doctor/fernandez-peter-md-122654', '/find-a-doctor/wolcott-susan-md-1734', '/find-a-doctor/weckesser-barry-md-2276', '/find-a-doctor/deputat-mikhail-md-19880', '/find-a-doctor/balzano-joseph-md-23821', '/find-a-doctor/farooq-ahmed-md-18713', '/find-a-doctor/mccormick-michael-dpm-11439', '/find-a-doctor/kaminski-joseph-do-14417', '/find-a-doctor/fitch-dwight-md-18457', '/find-a-doctor/raja-premala-md-7668', '/find-a-doctor/buckley-barbara-dpm-22285', '/find-a-doctor/piscitelli-ann-md-8218', '/find-a-doctor/kondrup-james-md-134308', '/find-a-doctor/hart-melinda-md-16337', '/find-a-doctor/lastomirsky-robert-md-13083', '/find-a-doctor/klutke-carl-md-13704', '/find-a-doctor/noah-joseph-md-9737', '/find-a-doctor/denholm-david-md-19910', '/find-a-doctor/gahhos-f-md-18016', '/find-a-doctor/elliott-lawrence-do-19072', '/find-a-doctor/bilal-jehanzeb-md-23134', '/find-a-doctor/galat-john-md-26850', '/find-a-doctor/bancroft-iii-josiah-md-135536', '/find-a-doctor/perdigon-rhoniel-md-8533', '/find-a-doctor/king-alan-do-13822', '/find-a-doctor/yan-david-md-32189', '/find-a-doctor/arabitg-gina-md-24343', '/find-a-doctor/johnson-mark-md-14756', '/find-a-doctor/ancheta-jullius-md-24488', '/find-a-doctor/miller-pamela-do-10849', '/find-a-doctor/llerena-lynette-do-12544', '/find-a-doctor/aguila-zenobio-md-24906', '/find-a-doctor/glover-jeffrey-do-17441', '/find-a-doctor/witkowski-edmund-md-1758', '/find-a-doctor/gonzalez-darsham-md-137578', '/find-a-doctor/bonjorno-jeremy-dpm-125892', '/find-a-doctor/roussillon-kristin-md-6527', '/find-a-doctor/dienes-robert-md-19698', '/find-a-doctor/gutierrez-mario-md-16813', '/find-a-doctor/lifton-allen-md-12687', '/find-a-doctor/raja-jay-md-7670', '/find-a-doctor/fraser-jeffrey-do-18188', '/find-a-doctor/soriano-andres-md-4580', '/find-a-doctor/templet-julie-md-3670', '/find-a-doctor/ruane-thomas-md-6477', '/find-a-doctor/shoemaker-david-md-5223', '/find-a-doctor/gallina-michael-dpm-17978', '/find-a-doctor/henriquez-omar-md-16056', '/find-a-doctor/mascola-trent-do-11703', '/find-a-doctor/koshy-mary-md-13544', '/find-a-doctor/vidolin-john-md-2715', '/find-a-doctor/landis-james-md-13165', '/find-a-doctor/felman-robert-md-18629', '/find-a-doctor/meurer-coatti-gabrielly-do-135541', '/find-a-doctor/roth-william-md-6546', '/find-a-doctor/khan-jaffer-md-14000', '/find-a-doctor/neily-john-do-9962', '/find-a-doctor/farris-karen-md-115291', '/find-a-doctor/fell-scott-do-18633', '/find-a-doctor/riveron-fernando-md-134493', '/find-a-doctor/savko-elizabeth-do-137530', '/find-a-doctor/arents-donald-md-24313', '/find-a-doctor/dumas-peter-md-19375', '/find-a-doctor/baga-melecito-md-23982', '/find-a-doctor/davenport-charles-md-20235', '/find-a-doctor/richey-hobart-md-7130', '/find-a-doctor/haghighi-tajvar-pouria-md-129986', '/find-a-doctor/demarco-hanna-md-19939', '/find-a-doctor/lough-eric-md-12405', '/find-a-doctor/ball-robert-do-23844', '/find-a-doctor/barnett-marguerite-md-23703', '/find-a-doctor/gero-michele-md-136825', '/find-a-doctor/cho-chung-hing-lorraine-md-21281', '/find-a-doctor/finley-christopher-chris-do-125720', '/find-a-doctor/glover-alan-md-17443', '/find-a-doctor/katz-michael-dpm-14257', '/find-a-doctor/majeed-farhan-md-36392', '/find-a-doctor/zagata-mateusz-md-34240', '/find-a-doctor/simovitz-ricky-md-5036', '/find-a-doctor/guerin-christopher-md-16928', '/find-a-doctor/knapp-alan-md-13699', '/find-a-doctor/reed-christopher-do-26804', '/find-a-doctor/abello-david-md-25199', '/find-a-doctor/hupp-bradley-md-15362', '/find-a-doctor/porter-alan-md-8071', '/find-a-doctor/reddy-dheeraj-md-100197', '/find-a-doctor/holguin-raul-md-15714', '/find-a-doctor/broadway-lauren-md-285', '/find-a-doctor/mcfadden-patrick-do-11373', '/find-a-doctor/silverman-larry-md-5079', '/find-a-doctor/shariff-sohail-md-5419', '/find-a-doctor/manickam-sampath-md-118889']

#for l in link:
#    rsp = requests.get(b + l, verify=False)
#    all_soup.append(rsp.text)


#soup_file = open("all_soup3", 'wb')
#marshal.dump(all_soup, soup_file)
#soup_file.close()

soup_file = open("all_soup3", 'rb')
all_soup=marshal.load(soup_file)
soup_file.close()

data=[]

j = 0
for text in all_soup:
    d = {}
    for i in range(38):
        d[i] = ''
    print(b + link[j])
    soup = BeautifulSoup(text, 'html.parser')

    h = json.loads(soup.find('script', type='application/ld+json').text)
    name = h['name'].split('\n')
    d[0] = name[2].split(',')[-1]
    d[1] = name[0]
    d[2] = name[1]

    loc = h['location']
    for l in loc:


    try:
        loc = soup.find("li", id="physicianLocations")
        print(loc.prettify())
        tmp = loc.find_all('span',class_='addr')
        p = 0
        for t in tmp:
            if t.get_text().find(', FL') != -1:
                break
            p += 1
        d[23] = tmp[p].get_text().strip().split(',')[-1]
        d[22] = tmp[p-1].get_text().strip()
        d[26] = tmp[p - 2].get_text().strip()
        if p-3 >=0:
            d[25] = tmp[p-3].get_text().strip()
        if len(tmp) > p :
            d[36] = tmp[p+1].get_text().strip()


        tmp = loc.find_all('span', class_='number')
        for t in tmp:
            if t.get_text().find('Phone') != -1:
                d[9] = t.get_text().split(':')[-1]
            if text.find('Fax') != -1:
                d[12] = t.get_text().split(':')[-1]
    except:
        print("FAIL " +  ' loc\n')

    d[35] = b + link[j]
    j += 1
    data.append(d)
write_excel(data)
# Page 1 -> Page 26
'''
done = ['Page 1']

def get_onepage():
    timeout = 30
    try:
        element_present = EC.presence_of_element_located((By.TAG_NAME, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")
    head = driver.find_element_by_class_name('pag-header')
    html = driver.page_source
    soup = BeautifulSoup(html)
    #print(soup)
    for link in soup.find_all('a'):
        if link.get('href'):
            if link.get('href').find('/find-a-doctor/') != -1:
                if link.get('href') not in all:
                    all.append(link.get('href'))
    elem = head.find_element_by_class_name('cpsty_PagerCurrentPage')
    print(elem.get_attribute('title'))

    next_sibling = driver.execute_script("""
    return arguments[0].nextElementSibling
""", elem)
    print(all)
    if elem.get_attribute('title') == 'Page 26':
        return
    next_sibling.click()
    time.sleep(10)
    get_onepage()


get_onepage()

'''

