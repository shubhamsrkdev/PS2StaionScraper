import csv
import xlwt
from bs4 import BeautifulSoup
from webbot import Browser
from tempfile import TemporaryFile

url = 'http://psd.bits-pilani.ac.in/Login.aspx'
web = Browser()
web.go_to(url)
web.type('PUT YOUR EMAIL HERE' , into = 'Username' , id = 'TxtEmail' )
web.type('PUT YOUR PASSWORD HERE', into = 'Password', id = 'txtPass')
web.click(id = 'Button1') ; 

url2 ='http://psd.bits-pilani.ac.in/Student/ViewActiveStationProblemBankData.aspx'
web.go_to(url2)
html = web.get_page_source()
soup = BeautifulSoup(html)

Stations = soup.find_all(id="stationname")
Locations = soup.find_all(id="lOCATION")
Domain = soup.find_all(id="Industry")
Accommodation = soup.find_all(id="ACCOMO")

StationNames = []
StationLocations = []
StationDomains = []
StationAccommodations = []

for stations in Stations:
	StationNames.append(stations.text)
for locations in Locations:
	StationLocations.append(locations.text)
for domain in Domain:
	StationDomains.append(domain.text)
for accommodation in Accommodation:
	StationAccommodations.append(accommodation.text.replace('-','Not Available'))


book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')


for i in range(len(StationNames)):
    sheet1.write(i,0,StationNames[i])
    sheet1.write(i,1,StationLocations[i])
    sheet1.write(i,2,StationDomains[i])
    sheet1.write(i,3,StationAccommodations[i])


name = "stations.xls"
book.save(name)
book.save(TemporaryFile())
	


