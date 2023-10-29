import requests
from  bs4 import BeautifulSoup
foundLİnk = []
target_url = "htpp://atilsamancioglu.com"
respose = requests.get(target_url)
soup1 = BeautifulSoup(respose.text)

for link in soup1.find_all("a"):
    found_list = link.get("href")
    if found_list not in  foundLİnk:
        foundLİnk.append(found_list)
        print(foundLİnk)






