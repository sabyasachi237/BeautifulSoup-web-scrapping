from bs4 import BeautifulSoup
#from csv import writer
import requests



url="https://www.amazon.in/?tag=admpdesktopin-21&ref=pd_sl_6bcd987c57d3578c0ea19bd72a11a6063eb7905c86eeaa0075356908&mfadid=adm"
page= requests.get(url)


Soup = BeautifulSoup(page.content, 'html.parser')
rows = Soup.find_all('div',id_="topsection")
# rows = Soup.find_all('div',class_="topsection")
print(rows)

     
#with open('new.csv','w', encoding='uft8',newline='') as f:

    #thewriter = writer(f)
    #header=['location','Residency','DocInfo','Education']
    # thewriter.writerow(header)
    # thewriter.writerow(header)
for row in rows:
    location=row.find('div',class_="Location__Wrapper-sc-5hr73o-0 gWcOly").text
    Residency=row.find('div',class_="ResidencySelection__Wrapper-sc-1neb61h-0 hGKZHE").text
    Education=row.find('div',class_="EducationSelection__Wrapper-sc-7266j1-0 cDpsCj").text
    DocInfo=row.find('div',class_="specialtiesWrapper").text

    info=[location,Residency,DocInfo,Education]
    print(row)
        #thewriter.writerow(info)
     
    






