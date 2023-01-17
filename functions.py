
import re
import requests
import urllib.parse
from config import BASE_URL


def get_all_places(city_id):
    url_fetch_all_places=f"{BASE_URL}/api/v1/Place/List"

    data={
    "filterInfo": [
        {
        "filterTerm": city_id,
        "filterType": "EQUALS",
        "filterBy": "cityId"
        },
        ]
    }

    res_places=requests.post(url_fetch_all_places,json=data)
    return res_places.json()
# aa=get_all_places("85ab5e34-3d98-406f-a8c1-77df8ed68c2c")
# print(len(aa["data"]))
def extract_email_phone_no(text):
  emails=[]
  email = re.findall(r'[\w\.-]+@[\w\.-]+', text)
  for i in email:
      if len(i)>10 and ".jpg" not in i:
          emails.append(i)
  
  return emails