
from config import BASE_URL
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import time
from functions import extract_email_phone_no, Increas_rating
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

def get_and_combine_all_data(url):
    facebook=[]
    twitter=[]
    instagram=[]
    email=[]
    tiktok=[]
    response = requests.get(url,headers=head)
    soup = BeautifulSoup(response.text, 'html.parser')
    url_regex = r"((https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))"
    all_urls=[]
    emails=extract_email_phone_no(str(soup))
    for em in emails:
        if em.lower() not in email:
            email.append(em.lower())
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            if url in href or href.startswith("/"):
                all_urls.append(href)
            if "facebook" in href:
                if href not in facebook:
                    facebook.append(href)
            elif "twitter" in href:
                if href not in twitter:
                    twitter.append(href)
            elif "instagram" in href:
                if href not in instagram:
                    instagram.append(href)
            elif "tiktok" in href:
                if href not in tiktok:
                    instagram.append(href)
    if facebook==[]:
        facebook.append("")
    if instagram==[]:
        instagram.append("")
    if twitter==[]:
        twitter.append("")
    if tiktok==[]:
        tiktok.append("")
    print("total urls found :- "+str(len(all_urls)))
    temp_url=[]
    port=0
    for i in all_urls:
        if i not in temp_url :
            temp_url.append(i)
            print(f"checking in url {i}.......................{len(all_urls)}")
            if i.startswith("/"):
                response = requests.get(url+i,headers=head)
            else:
                response = requests.get(i,headers=head)
                
            soup = BeautifulSoup(response.text, 'html.parser')
            emails=extract_email_phone_no(str(soup))
            for em in emails:
                if em.lower() not in email:
                    email.append(em.lower())
        port+=1
        if port>20:
            break
        else:
            pass
    # print(phone)       
    # print(email)       
    # print(instagram)
    # print(twitter)
    # print(facebook)           
    df={
        "Business":url,
        "instagram":instagram[0],
        "facebook":facebook[0],
        "twitter":twitter[0],
        "tiktok":tiktok[0],
        "email":email,
    }
    f=open("data.json","a",encoding="utf-8")
    f.write(str(df)+",")
    return df  
if __name__ == "__main__":
    names=[]
    categories=[]
    prize_ranges=[]
    ratings=[]
    review_n=[]
    addresses=[]
    Neighborhoods=[]
    states=[]
    cities=[]
    countries=[]
    zipcodes=[]
    latitudes=[]
    longitudes=[]
    phones=[]
    URL=[]
    facebooks=[]
    twitters=[]
    instagrams=[]
    emails=[]
    tiktoks=[]
    aa=Increas_rating()
    item_no=1
    all_dict=[]
    total=len(aa["data"])
    no=1
    for i in aa["data"]:
        try:
            print(f"Searching data for {item_no}/{total}")
            dD=urllib.parse.urlparse(str(i["FacebookLink"])) 
            base_url = dD.scheme + "://" +dD.netloc
            print(base_url)
            d=get_and_combine_all_data(base_url)
            out={
            "PlaceName":i['PlaceName'],
            "PlaceType":i['PlaceType'],
            "PriceRange":i['PriceRange'],
            "Rating":i['Rating'],
            "Rating_n":i['Rating_n'],
            "Address":i['Address'],
            "Neighborhood":i['Neighborhood'],
            "states":"",
            "cities":(i['Address']).split(",")[-2],
            "Country":i['Country'],
            "Latitude":i['Latitude'],
            "Longitude":i['Longitude'],
            "Zipcode":i['Zipcode'],
            "PhoneNumber":i['PhoneNumber'],
            "Business":d['Business'],
            "instagram":d['instagram'],
            "facebook":d['facebook'],
            "twitter":d['twitter'],
            "tiktok":d['tiktok'],
            "emails":str(d['email']).replace("'","").replace("[","").replace("]","")}
            print(out)
            # elapsed_time = time.time() - start_time  # Calculate elapsed time
            print("")
            print("")
            print("")
            print("")
            item_no+=1
            
            # if elapsed_time > 7200:  # If elapsed time is more than 2 hours (7200 seconds)
            #     break
        except:
            pass    
    # print(all_dict)
    for d in all_dict:
        URL.append(d['Business'])
        instagrams.append(d['instagram'])
        facebooks.append(d['facebook'])
        twitters.append(d['twitter'])
        emails.append(str(d['email']).replace("'","").replace("[","").replace("]",""))
    
    df=pd.DataFrame({
    "Business":URL,
    "instagram":instagrams,
    "facebook":facebooks,
    "twitter":twitters,
    "emails":emails,
})
    df.to_csv("Increase_Rating_contact_info.csv",index=False)
  



