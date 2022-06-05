
import requests

req = requests.get("https://www.trainman.in/services/trains/NDLS/BCT?key=012562ae-60a9-4fcd-84d6-f1354ee1ea48&sort=smart&meta=true&date=20-05-2022&class=ALL&quota=GN")
def minconverted(x):
    hr,min = list(map(lambda x: int(x),x.split(":")))
    return hr*60+min

minconverted("17:20")

    

if req.status_code == 200:
    data = req.json()
    # data['trains'][0].keys()
    # data['trains'][0]['pantry']
    
    sorted_train_data = sorted(data['trains'],key = lambda x: int(x['duration'].split(":")[0])*60 + int(x['duration'].split(":")[1]))
    
    sorted_train_data_pantry = list(filter(lambda x: x['pantry'] == 1,sorted_train_data))
    for i in sorted_train_data_pantry:
        print(f"Train Name : {i['tname']}, Duration : {i['duration']}")


        
        