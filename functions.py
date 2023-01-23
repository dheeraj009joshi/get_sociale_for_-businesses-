
import re
import requests
import urllib.parse
from config import BASE_URL


def places_without_website():
    url_fetch_all_places=f"{BASE_URL}/api/v1/Place/List"

    data={
      "filterInfo": [
        {
        "filterTerm": "",
        "filterBy": "FacebookLink",
        "filterType": "EQUALS"
        }
    ]
    }

    res_places=requests.post(url_fetch_all_places,json=data)
    return res_places.json()

def Increas_rating():
    url_fetch_all_places=f"{BASE_URL}/api/v1/Place/List"

    data={
      "filterInfo": [

{"filterBy": "Rating_n",
"filterTerm": "1",
"filterType": "GREATER"}, 

{"filterBy": "Rating_n",
"filterTerm": "50",
"filterType": "LESSER"}, 

{"filterBy": "Rating",
"filterTerm": "3.0",
"filterType": "LESSER"}, 
]
    }

    res_places=requests.post(url_fetch_all_places,json=data)
    return res_places.json()
# a=Increas_rating()
# print(a)

def extract_email_phone_no(text):
  emails=[]
  email = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)
  for i in email:
      if len(i)>10:
          emails.append(i)
  
  return emails