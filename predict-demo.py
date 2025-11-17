import requests


import json

# Path to your JSON file
json_file_path = 'demo_row.json'

# Open and load the JSON file
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

customer_id = data["leadid"]
customer = data["data"]
print(f"- Demo true conversion: {data["conversion_target"]}\n")

# # 22,32,Male,Islamabad,Social Media,60,15,Hot,4,Desktop,Facebook,1,2,0.1,14,4,115,Good,1
# customer_id = '22'
# customer = {
#     "gender": "male",
#     "location": "islamabad",
#     "leadsource": "social_media",
#     "leadstatus": "hot",
#     "devicetype": "desktop",
#     "referralsource": "facebook",
#     "paymenthistory": "good",
#     "age": 32,
#     "timespent_minutes": 60,
#     "pagesviewed": 15,
#     "emailsent": 4,
#     "formsubmissions": 1,
#     "downloads": 2,
#     "ctr_productpage": 0.1,
#     "responsetime_hours": 14,
#     "followupemails": 4,
#     "socialmediaengagement": 115
# }


url = 'http://localhost:9696/predict'

response = requests.post(url, json=customer).json()
print(response, end="\n\n")

if response['convert'] == True:
    print('sending Welcome email to LeadID - %s ...' % customer_id)
else:
    print('Customer %s didn\'t convert' % customer_id)