import json


with open('konular.json','r') as file:
    data = json.load(file)

dict = data


for icerik in data:
    print(icerik["kategori"]+"\t"+icerik["baslik"]+"\t"+icerik["tarih"])







