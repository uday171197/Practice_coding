import requests


headers = {'sso_token':'eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..yKJIT0fkHauPffOo.rReOmTtQAP7Yk9qDkhglp2uENnGkIMghZD7BsvyYdtsW9jU9_amUZ-TgYLbFWl2HTCb7mgvBzsAx0MFLFBBUDtQYDuQbvLHY7yegraFRw5i5Lf-o6gzPkBns4t9c_9U0lDiGWwkSSHbclRQBbgeZgmRxZVFd6CqTnOPEo0Wvb2OJYpM-jLU5xg5TLJOOk2y3Dlw29f_2WukAy_oXsLzUtLCAetsKEL_yeD-4qtWaF268AM_jWTxyAEi8sXTR5_3QEMV10Nk7C2HOQ1kkNpAW.tfe4wGt9MssCQ8_1CT5FRA9600'
           }

files = {'icon': open('file.txt','rb'),'request':open('file.txt','rb')}


res = requests.post('http://10.20.19.244:80/h5/v2/merchant/onboarding/app?app_id=b7270e73110248e88a6323a88a469c33',headers=headers,files=files)