import sys
import requests
from bs4 import BeautifulSoup
import csv



url = "http://www.thegradcafe.com/survey/index.php?t=n&pp=250&o=p"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "en-US,en;q=0.8",
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text,"html.parser")

for table_row in soup.select(".results tbody"):

    table_cells1 = table_row.findAll("tr",{"class":"row0"})        
    table_cells2 = table_row.findAll("tr",{"class":"row1"})

table_cells = table_cells1+table_cells2
#print(len(table_cells))
list1 = []

for i in table_cells:
    for p in i:
#        print(p.text.encode('cp1252','replace'))
        list1.append(p.text.encode('cp1252','replace'))


z=0
School =[]
Program =[]
Status=[]
for z in range(1500):
    if(z%6 == 0):
        School.append(list1[z])
    if(z%6 == 1):
        Program.append(list1[z])
    if(z%6 == 2):
        Status.append(list1[z])
School1=[]
Program1=[]
Status1=[]
for a in range(250):
    School1.append(School[a])#.decode("utf-8"))
    Program1.append(Program[a].decode("utf-8"))
#    print(len(School1))
#    print(len(Program1))
    Status1.append(Status[a])#.decode("utf-8"))
data = [['School', 'Program', 'Status']]
for k in range(240):
    data.append([School1[k],Program1[k],Status[k]])

#print(data.encode('cp1252','replace'))

with open('test.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data)

b = [['School', 'Program', 'Status']]
for s in data:
    if ((s[1].find("PROGRAM2")>=0) or (s[1].find("PROGRAM2")>=0)):	#replace 'PROGRAM' with the program of interest
        b.append([s[0],s[1],s[2]])

with open('test1.csv', 'w', newline='') as fp:
    c = csv.writer(fp, delimiter=',')
    c.writerows(b)
    
#print(b[0])
print(b)
