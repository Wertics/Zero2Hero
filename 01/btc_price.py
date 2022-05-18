import requests
import json


# Запушить в ветку изменения 
# Обоачивать все это в функции 
# узнаем что такое __main__ == "main"
# list 
# dict 
# dir(value)

res = requests.get ('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(res.text)

load_btc = json.loads(res.text)
# print (load_btc)

bpi_list = ("USD", "EUR")
btc_count = 10 

for i in load_btc["bpi"]:
    if i in bpi_list:
        btc_price = load_btc["bpi"][i]["rate"] 
        edited_btc_price = btc_price.replace(",", "")
        print(float(edited_btc_price) * btc_count)
    # print (i, load_btc["bpi"][i])

# bpi

# print (load_btc.get('USD', 'EUR'))
 
# dict["key2"]["key2.1"] 

# {
#     "key1" : {
#         "key1.1" : "value 1"
#         "key1.2" :  "value 2"
#     },
#     "key2" : {
#         "key2.1" : "value 21"
#         "key2.2" : "value 22"
#     } 


# }

# # load_btc
# for i in load_btc:
#     for k in load_btc[i]:
#         print(load_btc[i][k])