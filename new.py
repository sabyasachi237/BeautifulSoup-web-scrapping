from bs4 import BeautifulSoup
#from csv import writer
import requests
#import urlib2



url="https://intake.steerhealth.io/public-provider/aa1f8845b2eb62a957004eb491bb8ba70a/b818984b98e914a7423f6cbcd4a9b5db37"
page= requests.get(url)


Soup = BeautifulSoup(page.content, 'html.parser')
rows = Soup.find_all('div',class_="mainwrapper")
print(rows)
 
for row in rows:
    details=row.find('div',class_="details").text
    EducationAndResidency=row.find('div',class_="").text
    doctorInfo=row.find('div',class_="").text
    
    address=row.find('div',class_="LocationCard__Wrapper-sc-15q16f7-0 jAbTOx card location-card").text
    
    Residency=row.find('div',class_="").text
    


    print(doctorInfo)
    print(EducationAndResidency)
    print(details)
    # print(Education)

     