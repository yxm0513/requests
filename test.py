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
            print(k)
            sheet1.write(j, k, d[k])
        j += 1
    f.save('test.xls')



base = 'https://www.sccad.net/'
url = 'https://www.sccad.net/directorio-medico-sccad.php'

'''
rsp =  requests.get(url)
soup = BeautifulSoup(rsp.text, 'html.parser')
#print(soup.prettify())

url_list = []

for link in soup.find_all('a'):
    if link.get('href').find('directorio/') != -1:
        if link.get('href') not in url_list:
            url_list.append(link.get('href'))

#print(url_list)
all = []
for l in url_list:
    u = base + l
    rsp = requests.get(u)
    s = BeautifulSoup(rsp.text, 'html.parser')
    #print(s.prettify())
    for link in s.find_all('a'):
        if link.get('href').find('perfil.php?id') != -1:
            if link.get('href') not in all:
                all.append(link.get('href'))
'''
all = ['perfil.php?id=1676', 'perfil.php?id=1141', 'perfil.php?id=1142', 'perfil.php?id=1171', 'perfil.php?id=1185', 'perfil.php?id=1266', 'perfil.php?id=1265', 'perfil.php?id=1262', 'perfil.php?id=1270', 'perfil.php?id=1182', 'perfil.php?id=1224', 'perfil.php?id=1216', 'perfil.php?id=1170', 'perfil.php?id=1276', 'perfil.php?id=1274', 'perfil.php?id=1219', 'perfil.php?id=1263', 'perfil.php?id=1284', 'perfil.php?id=1581', 'perfil.php?id=1264', 'perfil.php?id=1212', 'perfil.php?id=1228', 'perfil.php?id=1209', 'perfil.php?id=1222', 'perfil.php?id=1273', 'perfil.php?id=1225', 'perfil.php?id=1272', 'perfil.php?id=1271', 'perfil.php?id=1283', 'perfil.php?id=1268', 'perfil.php?id=1269', 'perfil.php?id=1275', 'perfil.php?id=1144', 'perfil.php?id=1279', 'perfil.php?id=1232', 'perfil.php?id=1180', 'perfil.php?id=1277', 'perfil.php?id=1278', 'perfil.php?id=1267', 'perfil.php?id=1313', 'perfil.php?id=1301', 'perfil.php?id=1314', 'perfil.php?id=1296', 'perfil.php?id=1307', 'perfil.php?id=1286', 'perfil.php?id=1289', 'perfil.php?id=1293', 'perfil.php?id=1315', 'perfil.php?id=1310', 'perfil.php?id=1305', 'perfil.php?id=1291', 'perfil.php?id=1298', 'perfil.php?id=1299', 'perfil.php?id=1304', 'perfil.php?id=1311', 'perfil.php?id=1288', 'perfil.php?id=1285', 'perfil.php?id=1290', 'perfil.php?id=1306', 'perfil.php?id=1294', 'perfil.php?id=1302', 'perfil.php?id=1303', 'perfil.php?id=1297', 'perfil.php?id=1287', 'perfil.php?id=1312', 'perfil.php?id=1295', 'perfil.php?id=1300', 'perfil.php?id=1316', 'perfil.php?id=1', 'perfil.php?id=94', 'perfil.php?id=100', 'perfil.php?id=112', 'perfil.php?id=101', 'perfil.php?id=120', 'perfil.php?id=126', 'perfil.php?id=13', 'perfil.php?id=97', 'perfil.php?id=125', 'perfil.php?id=1052', 'perfil.php?id=89', 'perfil.php?id=106', 'perfil.php?id=102', 'perfil.php?id=84', 'perfil.php?id=87', 'perfil.php?id=85', 'perfil.php?id=72', 'perfil.php?id=1138', 'perfil.php?id=88', 'perfil.php?id=90', 'perfil.php?id=666', 'perfil.php?id=1133', 'perfil.php?id=1139', 'perfil.php?id=93', 'perfil.php?id=95', 'perfil.php?id=98', 'perfil.php?id=96', 'perfil.php?id=103', 'perfil.php?id=99', 'perfil.php?id=1134', 'perfil.php?id=105', 'perfil.php?id=91', 'perfil.php?id=107', 'perfil.php?id=1673', 'perfil.php?id=108', 'perfil.php?id=109', 'perfil.php?id=1683', 'perfil.php?id=1136', 'perfil.php?id=1140', 'perfil.php?id=111', 'perfil.php?id=113', 'perfil.php?id=114', 'perfil.php?id=115', 'perfil.php?id=1257', 'perfil.php?id=1334', 'perfil.php?id=1370', 'perfil.php?id=1341', 'perfil.php?id=1337', 'perfil.php?id=1371', 'perfil.php?id=1356', 'perfil.php?id=1367', 'perfil.php?id=1354', 'perfil.php?id=1373', 'perfil.php?id=1351', 'perfil.php?id=1366', 'perfil.php?id=1335', 'perfil.php?id=1325', 'perfil.php?id=1352', 'perfil.php?id=1327', 'perfil.php?id=1328', 'perfil.php?id=1358', 'perfil.php?id=1339', 'perfil.php?id=1333', 'perfil.php?id=1320', 'perfil.php?id=1324', 'perfil.php?id=1368', 'perfil.php?id=1332', 'perfil.php?id=1336', 'perfil.php?id=1348', 'perfil.php?id=1347', 'perfil.php?id=1364', 'perfil.php?id=1318', 'perfil.php?id=1321', 'perfil.php?id=1349', 'perfil.php?id=1360', 'perfil.php?id=1353', 'perfil.php?id=1363', 'perfil.php?id=1365', 'perfil.php?id=1374', 'perfil.php?id=1338', 'perfil.php?id=1350', 'perfil.php?id=1344', 'perfil.php?id=1346', 'perfil.php?id=1369', 'perfil.php?id=1331', 'perfil.php?id=1359', 'perfil.php?id=1322', 'perfil.php?id=1362', 'perfil.php?id=1355', 'perfil.php?id=1361', 'perfil.php?id=1345', 'perfil.php?id=1329', 'perfil.php?id=1317', 'perfil.php?id=1340', 'perfil.php?id=1342', 'perfil.php?id=1343', 'perfil.php?id=1372', 'perfil.php?id=1323', 'perfil.php?id=1326', 'perfil.php?id=1357', 'perfil.php?id=1330', 'perfil.php?id=1319', 'perfil.php?id=1445', 'perfil.php?id=1258', 'perfil.php?id=1382', 'perfil.php?id=1379', 'perfil.php?id=1383', 'perfil.php?id=1377', 'perfil.php?id=1421', 'perfil.php?id=1446', 'perfil.php?id=1402', 'perfil.php?id=1407', 'perfil.php?id=1380', 'perfil.php?id=1376', 'perfil.php?id=1381', 'perfil.php?id=1411', 'perfil.php?id=1390', 'perfil.php?id=1417', 'perfil.php?id=1418', 'perfil.php?id=1389', 'perfil.php?id=1424', 'perfil.php?id=1399', 'perfil.php?id=1419', 'perfil.php?id=1392', 'perfil.php?id=1444', 'perfil.php?id=1409', 'perfil.php?id=1401', 'perfil.php?id=1413', 'perfil.php?id=1416', 'perfil.php?id=1423', 'perfil.php?id=1443', 'perfil.php?id=1426', 'perfil.php?id=1386', 'perfil.php?id=1404', 'perfil.php?id=1394', 'perfil.php?id=1415', 'perfil.php?id=1388', 'perfil.php?id=1420', 'perfil.php?id=1375', 'perfil.php?id=1397', 'perfil.php?id=1412', 'perfil.php?id=1440', 'perfil.php?id=1425', 'perfil.php?id=1396', 'perfil.php?id=1398', 'perfil.php?id=1403', 'perfil.php?id=1427', 'perfil.php?id=1384', 'perfil.php?id=1441', 'perfil.php?id=1410', 'perfil.php?id=1406', 'perfil.php?id=1378', 'perfil.php?id=1408', 'perfil.php?id=1387', 'perfil.php?id=1385', 'perfil.php?id=1395', 'perfil.php?id=1391', 'perfil.php?id=1422', 'perfil.php?id=1393', 'perfil.php?id=1405', 'perfil.php?id=1400', 'perfil.php?id=1414', 'perfil.php?id=1511', 'perfil.php?id=1259', 'perfil.php?id=1457', 'perfil.php?id=1502', 'perfil.php?id=1437', 'perfil.php?id=1451', 'perfil.php?id=1455', 'perfil.php?id=1460', 'perfil.php?id=1459', 'perfil.php?id=1430', 'perfil.php?id=1449', 'perfil.php?id=1507', 'perfil.php?id=1499', 'perfil.php?id=1480', 'perfil.php?id=1464', 'perfil.php?id=1452', 'perfil.php?id=1454', 'perfil.php?id=1482', 'perfil.php?id=1465', 'perfil.php?id=1492', 'perfil.php?id=1506', 'perfil.php?id=1483', 'perfil.php?id=1458', 'perfil.php?id=1495', 'perfil.php?id=1432', 'perfil.php?id=1479', 'perfil.php?id=1504', 'perfil.php?id=1496', 'perfil.php?id=1497', 'perfil.php?id=1481', 'perfil.php?id=1476', 'perfil.php?id=1488', 'perfil.php?id=1439', 'perfil.php?id=1487', 'perfil.php?id=1470', 'perfil.php?id=1461', 'perfil.php?id=1463', 'perfil.php?id=1462', 'perfil.php?id=1498', 'perfil.php?id=1471', 'perfil.php?id=1466', 'perfil.php?id=1435', 'perfil.php?id=1434', 'perfil.php?id=1508', 'perfil.php?id=1491', 'perfil.php?id=1448', 'perfil.php?id=1436', 'perfil.php?id=1500', 'perfil.php?id=1485', 'perfil.php?id=1509', 'perfil.php?id=1474', 'perfil.php?id=1438', 'perfil.php?id=1433', 'perfil.php?id=1490', 'perfil.php?id=1503', 'perfil.php?id=1486', 'perfil.php?id=1456', 'perfil.php?id=1467', 'perfil.php?id=1494', 'perfil.php?id=1510', 'perfil.php?id=1468', 'perfil.php?id=1429', 'perfil.php?id=1489', 'perfil.php?id=1428', 'perfil.php?id=1484', 'perfil.php?id=1501', 'perfil.php?id=1478', 'perfil.php?id=1472', 'perfil.php?id=1493', 'perfil.php?id=1477', 'perfil.php?id=1450', 'perfil.php?id=1453', 'perfil.php?id=1475', 'perfil.php?id=1469', 'perfil.php?id=1473', 'perfil.php?id=1431', 'perfil.php?id=1549', 'perfil.php?id=1260', 'perfil.php?id=1261', 'perfil.php?id=1569', 'perfil.php?id=1570', 'perfil.php?id=1539', 'perfil.php?id=1514', 'perfil.php?id=1537', 'perfil.php?id=1538', 'perfil.php?id=1544', 'perfil.php?id=1556', 'perfil.php?id=1550', 'perfil.php?id=1548', 'perfil.php?id=1536', 'perfil.php?id=1530', 'perfil.php?id=1529', 'perfil.php?id=1528', 'perfil.php?id=1540', 'perfil.php?id=1542', 'perfil.php?id=1520', 'perfil.php?id=1521', 'perfil.php?id=1522', 'perfil.php?id=1523', 'perfil.php?id=1525', 'perfil.php?id=1524', 'perfil.php?id=1526', 'perfil.php?id=1518', 'perfil.php?id=1513', 'perfil.php?id=1512', 'perfil.php?id=1519', 'perfil.php?id=1516', 'perfil.php?id=1517', 'perfil.php?id=1527', 'perfil.php?id=1531', 'perfil.php?id=1572', 'perfil.php?id=1553', 'perfil.php?id=1551', 'perfil.php?id=1574', 'perfil.php?id=1562', 'perfil.php?id=1576', 'perfil.php?id=1555', 'perfil.php?id=1578', 'perfil.php?id=1577', 'perfil.php?id=1546', 'perfil.php?id=1559', 'perfil.php?id=1552', 'perfil.php?id=1543', 'perfil.php?id=1532', 'perfil.php?id=1534', 'perfil.php?id=1535', 'perfil.php?id=1565', 'perfil.php?id=1567', 'perfil.php?id=1575', 'perfil.php?id=1533', 'perfil.php?id=1558', 'perfil.php?id=1554', 'perfil.php?id=1545', 'perfil.php?id=1566', 'perfil.php?id=1557', 'perfil.php?id=1515', 'perfil.php?id=1571', 'perfil.php?id=1568', 'perfil.php?id=1573', 'perfil.php?id=1541', 'perfil.php?id=1560', 'perfil.php?id=1161', 'perfil.php?id=1149', 'perfil.php?id=1223', 'perfil.php?id=1214', 'perfil.php?id=1255', 'perfil.php?id=1173', 'perfil.php?id=1177', 'perfil.php?id=1167', 'perfil.php?id=1148', 'perfil.php?id=1252', 'perfil.php?id=1172', 'perfil.php?id=1146', 'perfil.php?id=1181', 'perfil.php?id=1226', 'perfil.php?id=1217', 'perfil.php?id=1158', 'perfil.php?id=1190', 'perfil.php?id=1218', 'perfil.php?id=1157', 'perfil.php?id=1178', 'perfil.php?id=1221', 'perfil.php?id=1227', 'perfil.php?id=1150', 'perfil.php?id=1199', 'perfil.php?id=1231', 'perfil.php?id=1174', 'perfil.php?id=1198', 'perfil.php?id=1237', 'perfil.php?id=1236', 'perfil.php?id=1238', 'perfil.php?id=1153', 'perfil.php?id=1155', 'perfil.php?id=1176', 'perfil.php?id=1234', 'perfil.php?id=1204', 'perfil.php?id=1163', 'perfil.php?id=1239', 'perfil.php?id=1183', 'perfil.php?id=1189', 'perfil.php?id=1211', 'perfil.php?id=1230', 'perfil.php?id=1253', 'perfil.php?id=1240', 'perfil.php?id=1152', 'perfil.php?id=1203', 'perfil.php?id=1175', 'perfil.php?id=1205', 'perfil.php?id=1159', 'perfil.php?id=1202', 'perfil.php?id=1187', 'perfil.php?id=1197', 'perfil.php?id=1241', 'perfil.php?id=1188', 'perfil.php?id=1191', 'perfil.php?id=1179', 'perfil.php?id=1151', 'perfil.php?id=1147', 'perfil.php?id=1184', 'perfil.php?id=1165', 'perfil.php?id=1242', 'perfil.php?id=1210', 'perfil.php?id=1195', 'perfil.php?id=1192', 'perfil.php?id=1254', 'perfil.php?id=1213', 'perfil.php?id=1168', 'perfil.php?id=1145', 'perfil.php?id=1201', 'perfil.php?id=1243', 'perfil.php?id=1256', 'perfil.php?id=1235', 'perfil.php?id=1196', 'perfil.php?id=1166', 'perfil.php?id=1193', 'perfil.php?id=1208', 'perfil.php?id=1244', 'perfil.php?id=1162', 'perfil.php?id=1215', 'perfil.php?id=1169', 'perfil.php?id=1156', 'perfil.php?id=1186', 'perfil.php?id=1207', 'perfil.php?id=1194', 'perfil.php?id=1206', 'perfil.php?id=1160', 'perfil.php?id=1154', 'perfil.php?id=1233', 'perfil.php?id=1229', 'perfil.php?id=1200', 'perfil.php?id=1245', 'perfil.php?id=1246', 'perfil.php?id=1220', 'perfil.php?id=1164', 'perfil.php?id=1247']
#all = ['perfil.php?id=1261', 'perfil.php?id=1676', 'perfil.php?id=1141']
#print(all)

data = []
for a in all:
    text = ''
    d = {}
    for i in range(34):
        d[i] = ''
    u =  base + '/directorio/' + a
    rsp = requests.get(u)
    soup = BeautifulSoup(rsp.text, 'html.parser')
    name = soup.find('span',class_="mid")
    text += name.get_text()
    tmp = name.get_text().split(' ')
    if tmp[0].find('Dr') != -1:
        d[1] = tmp[0].strip()
        tmp.pop(0)
    d[2] = tmp[0].strip()
    d[3] = ''.join(tmp[1:]).strip()
    address = soup.find("address")
    text += address.get_text()
    #
    d[18] = 'Asociación Panameña de Dermatologia'
    tmp = address.get_text().split('\n')
    d[24] = tmp[2].strip()
    d[20] = tmp[3].strip().split(',')[0]
    d[19] = tmp[4].strip()
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
        if l.get('href').find('tel:') != -1:
            d[7 + indext] = l.get('href').split(':')[1]
            indext += 1
            continue
        if l.get('href').find('http') != -1:
            d[28] = l.get('href')

    d[0] = text
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