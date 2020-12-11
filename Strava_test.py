
# coding: utf-8

# In[1]:


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# In[2]:


auth_url="https://www.strava.com/oauth/token"
#?client_id=57098&client_secret=3d0135bcb98b14e1cd9e7b78ae9d7eb219e5b312&code=bdb3e7a89da0eb4bb1c5a2c4ae99e1abaa4d56a9&grant_type=authorization_code

payload = {
    'client_id': "57098",
    'client_secret': '3d0135bcb98b14e1cd9e7b78ae9d7eb219e5b312',
    'refresh_token': 'b005696cc90eff78e0bdb34341f0406e5ef85b4d',
    'grant_type': 'refresh_token',
    'f': 'json'
}
print("Requesting Token...\n")
res = requests.post(auth_url,data=payload,verify=False)
Access_token=res.json()['access_token']
print("Access_token = {}...\n".format(Access_token))
## ça ça marche !
#print(res.json())
#f2800ccb3242eb26a315f3c16d91ef84b94827df
#https://www.strava.com/oauth/token?client_id=57098&client_secret=3d0135bcb98b14e1cd9e7b78ae9d7eb219e5b312&refresh_token=f2800ccb3242eb26a315f3c16d91ef84b94827df&grant_type=refresh_token


# In[3]:


activities_url = "https://www.strava.com/api/v3/athlete/activities"
print(activities_url)

header = {'Authorization': 'Bearer ' + Access_token}
print(header)

param = {'access_token': Access_token, 'per_page': 200, 'page': 1}
print(param)

#print(requests.get(activities_url,headers=header,params=param).json())

stravdata = requests.get(url=activities_url, headers=header, params=param).json()
print(stravdata)

