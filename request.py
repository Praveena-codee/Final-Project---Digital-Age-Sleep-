import requests
#return requests.get(url).json()


url = 'http://127.0.0.1:5000'
r = requests.POST(url,json={'activities':1, 'devicesBR':7, 'devicescount':0, 'usage':0, 'Rules':0, 'enforce':1, 'behaviour':7, 'rate':8})

print(r.json())

# # {
#   ...
#   "form": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   ...
# }

# host_url = "http://127.0.0.1:5000"

# # get the data
# data_for_prediction = [int(input()) for _ in range(10)]
# r = requests.post(url=host_url,json={data_for_prediction})
# print(r.json())