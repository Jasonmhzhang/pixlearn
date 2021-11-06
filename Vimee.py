import json
import requests
import re

url='https://www.youneed.win/wp-admin/admin-ajax.php'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73',
         # 'referer': 'https://www.youneed.win/free-v2ray',
         'referer': 'https://www.youneed.win/free-v2ray/comment-page-4',
         'cookie': 'gothamadblock_last_visit_time=1; _ga=GA1.2.1272019522.1629860828; _gid=GA1.2.874471133.1629860828; _gat_gtag_UA_138692554_1=1'
         }
data={'action':'validate_input',
      'nonce':'ed9049fda0',
      'captcha':'success',
      'post_id':'563',
      'type':'captcha',
      'portection':''
      }

resp=requests.post(url=url,headers=headers,data=data)
data=resp.json()['content']
pattern='data-raw="(.+?)"'
res1=re.findall(pattern,data,flags=0)
with open('vmess5.txt','w') as f:
    for res in res1:
        # print(res)
        f.write(f'{res}\n')


# file='vm.json'
# data=open(file,'rb')
# pattern='data-raw="(.+?)"'
# for seg in data:
#     vms=json.loads(seg)
#     str1=vms['content']
#     # print(str1)
#     result=re.findall(pattern,str1,flags=0)
#     for m in result:
#         print(m)

