from data import all_data
import pandas as pd
URL=[]
facebooks=[]
twitters=[]
instagrams=[]
emails=[]




for d in all_data:
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
  