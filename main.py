
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
    f.write(str(df))
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
    Email_final=[]
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
            web_name=base_url.split("/")[2].split(".")[-2]
            print("website name = ",web_name)
            f_mail_bets=[]
            try:
                for e in d['email']: 
                    if web_name in e:
                        print("name of website found in email :- ", e)
                        f_mail_bets.append(e)
            except Exception as err:
                print(err)
                pass
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
            "emails":d['email'],
            "F_mail":f_mail_bets}
            
            print(out)
            all_dict.append(out)
                            
        except Exception as err:
            print ( "err caucing the problem ",err)
            if str(err)=="No connection adapters were found for '://'":
                print(" No website url available ")
                pass
            elif requests.exceptions.ConnectionError:
                print("http err ")
                print("Connection refused by the server..")
                # print("Let me sleep for 5 minuter ")
                # print("ZZzzzz...")
                # time.sleep(300)
                # print("Was a nice sleep, now let me continue...")
                continue
                # pass
            else:
                print(str(err))
                pass
            # print(err)
            
        item_no+=1
        no+=1
        # if no>10:
        #     break
        
    

    print(len(all_dict))
    for i in all_dict:
            try:
                print("in try ")

                F_EMAIL=i["F_mail"][0] 
            except :
                F_EMAIL=""
            names.append(i['PlaceName'])
            categories.append(i['PlaceType'])
            prize_ranges.append(i['PriceRange'])
            ratings.append(i['Rating'])
            review_n.append(i['Rating_n'])
            addresses.append(i['Address'])
            Neighborhoods.append(i['Neighborhood'])
            states.append("")
            cities.append(i["cities"])
            countries.append(i['Country'])
            latitudes.append(i['Latitude'])
            longitudes.append(i['Longitude'])
            zipcodes.append(i['Zipcode'])
            phones.append(i['PhoneNumber'])
            URL.append(i['Business'])
            instagrams.append(i['instagram'])
            facebooks.append(i['facebook'])
            twitters.append(i['twitter'])
            tiktoks.append(i['tiktok'])
            emails.append(str(i["emails"]).replace("'","").replace("[","").replace("]",""))
            Email_final.append(F_EMAIL)
          

            
            
    print(len(names))     
    print(len(categories))     
    print(len(prize_ranges))     
    print(len(review_n))     
    print(len(addresses))     
    print(len(Neighborhoods))     
    print(len(cities))     
    print(len(states))     
    print(len(countries))     
    print(len(zipcodes))     
    print(len(latitudes))     
    print(len(longitudes))     
    print(len(URL))     
    print(len(instagrams))     
    print(len(facebooks))     
    print(len(twitters))     
    print(len(tiktoks))          
    df=pd.DataFrame(
    {
    "Business Name": names,
    "Category": categories,
    "Price": prize_ranges,
    "Rating": ratings,
    "Review Count": review_n,
    "Address": addresses,
    "Neighborhood": Neighborhoods,
    "City": cities,
    "State": states,
    "Country": countries,
    "Zipcode": zipcodes,
    "Latitude":latitudes,
    "Longitude": longitudes,
    "Phone Number": phones,
    "Email": emails,
    "Website":URL,
    "Instagram":instagrams,
    "Facebook": facebooks,
    "Twitter": twitters,
    "Tiktok": tiktoks
})
   
    
    
    df_final=pd.DataFrame(
    {
    "Business Name": names,
    "Category": categories,
    "Price": prize_ranges,
    "Rating": ratings,
    "Review Count": review_n,
    "Address": addresses,
    "Neighborhood": Neighborhoods,
    "City": cities,
    "State": states,
    "Country": countries,
    "Zipcode": zipcodes,
    "Latitude":latitudes,
    "Longitude": longitudes,
    "Phone Number": phones,
    "Email": Email_final,
    "Website":URL,
    "Instagram":instagrams,
    "Facebook": facebooks,
    "Twitter": twitters,
    "Tiktok": tiktoks
})
    df.to_csv("Increase_Rating_contact_info.csv",index=False)
    df_final.to_csv("Increase_Rating_final_output.csv",index=False)
  



