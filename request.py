
import requests as req
import json
from pandas.core.frame import DataFrame
url="https://www.twse.com.tw/fund/BFI82U?response=json&dayDate=&weekDate=&monthDate=&type=day&_"
res=req.get(url)
res.text
s=json.loads(res.text)
list=[]
for data in (s['data']):
    list.append(data)
data=DataFrame(list)
data.rename(columns={0:'單位名稱',1:'買進金額',2:'賣出金額',3:'買賣差額'},inplace=True)
data=data.set_index("單位名稱")
print(data)
