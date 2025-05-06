#scraping booking.com data

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time
url='https://www.booking.com/searchresults.en-gb.html?ss=Melbourne+CBD&ssne=Melbourne+CBD&ssne_untouched=Melbourne+CBD&label=en-au-booking-desktop-NG5ZKhQc*lZ*DP_1zn8GPAS652796015697%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9071443%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=1593&dest_type=district&checkin=2025-06-01&checkout=2025-06-02&group_adults=2&no_rooms=1&group_children=0'

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

def web_scraper(url,file_name):
    response=requests.get(url,headers=header)

    if response.status_code==200:
        print("Connection Successful")
        html_content=response.text

        time.sleep(5)

        soup=BeautifulSoup(html_content,"lxml")
        hotel_divs=soup.find_all("div",role="listitem")

        with open(f"{file_name}.csv","w") as file_csv:
            
            writer=csv.writer(file_csv)
            writer.writerow(['Hotel','Location','Price','Rating','Score','Number of Reviews','Room Type','Link'])

            for hotel in hotel_divs:
                hotel_name=hotel.find('div',class_="b87c397a13 a3e0b4ffd1").text.strip()
                hotel_name if hotel_name else "NA"
                price=hotel.find("span",class_="b87c397a13 f2f358d1de ab607752a2").text.strip()
                price if price else "NA"
                location=hotel.find("span",class_='d823fbbeed f9b3563dd4').text.strip()
                location if location else "NA"
                num_reviews=hotel.find("div",class_='fff1944c52 fb14de7f14 eaa8455879').text.strip().replace(' reviews','')
                num_reviews if num_reviews else "NA"
                score=hotel.find("div",class_="f63b14ab7a dff2e52086").text.strip()
                score if score else "NA"
                rating=hotel.find("div",class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
                rating if rating else "NA"
                room_type=hotel.find("h4",class_="fff1944c52 f254df5361").text.strip()
                room_type if room_type else "NA"
                # hotel_star=hotel.find("div",class_="b5ab46c480").text
                link=hotel.find("a",href=True).get('href')
                link if link else "NA"
                writer.writerow([hotel_name,location,price,rating,score,num_reviews,room_type,link])
        print("Data Exported as CSV")
    else:
        print("Connection Unsuccessful")


if __name__=='__main__':
    url=input("Enter the url:")
    file_name=input("Enter the File Name:")
    web_scraper(url,file_name)