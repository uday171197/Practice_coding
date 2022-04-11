import openpyxl
import pandas as pd
import requests
from  tqdm import tqdm
import base64



def get_request(api_id):
    headers = {
        "client_id":"jay-client-id2",
        "sso_token":'eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..zpTXAQ7Rv7_5C7ot.i-V48fyXq65i-AuvK6394WHpmDkNlR5wq7sT6FPDDo1o0ydS__JXpOXho5BPoJOlTK5jT-D2em9KS5A0t1vYChWLuX3LX2JzCuSk5gh9as16SKmibTSjRXb3gvFhY5ZP-irNrH6uHOe8CXQ45C_W_9L4bKUuLZGIUEs4H8HSq9lPg8Jz9shFlEo8eor_OK35HH18OU_gM1DusbpFbpMdiL-4f2W-MlKJgc8rPXAbMkxzIz1HmdjbDTQAgIfEdLahRq2PY9FVqfK4JqWC.8JX9rKVi3pb5nTZGyOUahg7800',
        "Cookie":"ff.sid=s%3A7HShvp00uWA_6Q4ZTjaXRbNAOzL7-xZk.F2aO98wrD42YJCOxF%2B1yj9Tlc1eMufp%2FMXebtkmmibI"
                    }
    
    res = requests.get(f'http://10.20.19.244:80/h5/v2/merchant/onboarding/app?app_id={api_id}',headers=headers)
    if res.status_code == 200:
        return True, res.text
    else:
        return False,""
    
def post_request(image_path,api_id):
    headers = {'sso_token':'eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..yKJIT0fkHauPffOo.rReOmTtQAP7Yk9qDkhglp2uENnGkIMghZD7BsvyYdtsW9jU9_amUZ-TgYLbFWl2HTCb7mgvBzsAx0MFLFBBUDtQYDuQbvLHY7yegraFRw5i5Lf-o6gzPkBns4t9c_9U0lDiGWwkSSHbclRQBbgeZgmRxZVFd6CqTnOPEo0Wvb2OJYpM-jLU5xg5TLJOOk2y3Dlw29f_2WukAy_oXsLzUtLCAetsKEL_yeD-4qtWaF268AM_jWTxyAEi8sXTR5_3QEMV10Nk7C2HOQ1kkNpAW.tfe4wGt9MssCQ8_1CT5FRA9600'
                    }
    files = {'icon': open(image_path,'rb')}
    # files = {'icon': open(image_path,'rb'),'request':open('file.txt','rb')}
    res = requests.post(f'http://10.20.19.244:80/h5/v2/merchant/onboarding/app?app_id={api_id}',headers=headers,files=files)
    if res.status_code == 200:
        print(f'Process Complete for api_id : {api_id}')
    else:
        print(f'Error in post api call for api_id : {api_id}')

def main():
    # data1 = pd.read_excel(r'New_Query_2022_03_10.xlsx',engine='openpyxl')

    data1 = pd.read_excel(r'New_Query_2022_03_16 (1).xlsx',engine='openpyxl')
    for index, url in tqdm(enumerate(data1.iloc[:,7])):
        if not isinstance(url,float) and 'http' not in url:
            
            try:
                url_lits = url.split(';')
                image_type = url_lits[0].split(':')[1].split('/')[1]
                baseb4_value = url_lits[1].split(',')[1]
                baseb4_value = bytes(baseb4_value, 'utf-8')
                image_64_decode = base64.decodestring(baseb4_value) 
                image_path = f'image/{data1.iloc[index,0]}.{image_type}'
                image_result = open(image_path, 'wb') # create a writable image and write the decoding result
                image_result.write(image_64_decode)
                api_id = data1.iloc[index,2]
                print(image_path,api_id)
                flag,request_data = get_request(api_id)
                if flag:
                    post_request(image_path,api_id)
                else:
                    print(f'Error in get api call for api id : {api_id}')
            except: pass
        
        
main()
