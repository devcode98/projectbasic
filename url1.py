import urllib.request
response=urllib.request.urlopen("https://data.gov.in/node/5073441/datastore/export/json") # through this command we just got the data directly
x=response.read()
#https://ipinfo.io/8.8.8.8/geo?token=4aa4c67fe8dfd9

print(x)
