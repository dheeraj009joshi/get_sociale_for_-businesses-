
from config import BASE_URL
import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import time
from functions import extract_email_phone_no, get_all_places
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
# social_media = ['facebook', 'twitter', 'instagram', 'linkedin', 'pinterest', 'youtube']
def get_and_combine_all_data(url):
    facebook=[]
    twitter=[]
    instagram=[]
    email=[]
    phone=[]
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
    if facebook==[]:
        facebook.append("")
    if instagram==[]:
        instagram.append("")
    if twitter==[]:
        twitter.append("")
    print("total urls found :- "+str(len(all_urls)))
    for i in all_urls:
        if i.startswith("/"):
            response = requests.get(url+i,headers=head)
        else:
            response = requests.get(i,headers=head)
            
        soup = BeautifulSoup(response.text, 'html.parser')
        emails=extract_email_phone_no(str(soup))
        for em in emails:
            if em.lower() not in email:
                email.append(em.lower())
        
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
        "email":email,
    }
    f=open("data.json","a",encoding="utf-8")
    f.write(str(df)+",")
    return df  
if __name__ == "__main__":
    start_time=time.time()
    # city_id= "85ab5e34-3d98-406f-a8c1-77df8ed68c2c"
    # res=get_all_places(city_id)
    URL=[]
    facebooks=[]
    twitters=[]
    instagrams=[]
    emails=[]
    # try:
    aa=get_all_places("85ab5e34-3d98-406f-a8c1-77df8ed68c2c")
    all_dict=[]
    # inr=0
    item_no=1
    total=len(aa["data"])
    print(len(aa["data"]))
    for i in aa["data"]:
        try:
            print(f"Searching data for {item_no}/{total}")
            d=urllib.parse.urlparse(str(i["FacebookLink"])) 
            base_url = d.scheme + "://" +d.netloc
            print(base_url)
            # url = 'http://bay6chennai.com/'
            out=get_and_combine_all_data(base_url)
            all_dict.append(out)
            print(out)
            elapsed_time = time.time() - start_time  # Calculate elapsed time
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
    df.to_csv("output_info.csv")
  

