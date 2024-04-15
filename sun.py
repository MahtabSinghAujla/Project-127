from bs4 import BeautiftrSoup
import time
import csv
import requests

start_url='https://en.wikipedia.org/wiki/List_of_brightest_stars'
time.sleep(10)

def scrape_more_data(hyperlink) :
    try :
        page=requests.get(hyperlink)
        soup=BeautiftrSoup(page.content,'html.parser')
        temp_list=[]
        for tr_tag in soup.find_all('tr',attrs={'class':'fact_row'}):
            td_tags=tr_tag.find_all('td')
            for td_tag in td_tags :
                try :
                    temp_list.append(td_tag.find_all('div',attrs={'class':'value'})[0].contents[0])
                except :
                    temp_list.append('')
        new_planets_data.append(temp_list)
    except :
        time.sleep(1)
        scrape_more_data(hyperlink)

def scrape():
    headers=['name','light_years_from_earth','star_mass','star_radius']
    planet_data=[]
    for i in range(0,428) :
        soup=BeautiftrSoup(start_url,'html.parser')
        for tr_tag in soup.find_all('tr',attrs={'class','exoplanet'}) :
            td_tags=tr_tag.find_all('td')
            temp_list=[]
            for index,tr_tag in enumerate(td_tags) :
                if index==0 :
                    temp_list.append(tr_tag.find_all('a')[0].contents[0])
                else :
                    try :
                        temp_list.append(tr_tag.content[0])
                    except :
                        temp_list.append('')
            hyperlink_tr_tag=td_tags[0]
            temp_list.append('https://en.wikipedia.com'+hyperlink_tr_tag.find_all('a',href='True')[0]['href'])
            planet_data.append(temp_list)
    with open('data.csv','w') as f :
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()
