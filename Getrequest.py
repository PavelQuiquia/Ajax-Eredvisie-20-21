import requests
import json
import pandas as pd

url = "https://www.whoscored.com/StatisticsFeed/1/GetPlayerStatistics?category=summary&subcategory=all&statsAccumulationType=0&isCurrent=true&playerId=&teamIds=130&matchId=&stageId=&tournamentOptions=13&sortBy=Rating&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=Overall&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=false&page=&includeZeroValues=true&numberOfPlayersToPick="

payload={}
headers = {
  'authority': 'www.whoscored.com',
  'pragma': 'no-cache',
  'cache-control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'model-last-mode': '07UjZ0R3wDqChdB/M+/EOIw6sZo0f37JQeikRZJJSPE=',
  'x-requested-with': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.whoscored.com/Teams/130/Show/Netherlands-Ajax',
  'accept-language': 'es-ES,es;q=0.9,en;q=0.8,nl;q=0.7',
  'cookie': 'visid_incap_774906=UKHr453XRyy7DMnowSyRgZPIVGAAAAAAQUIPAAAAAADyt5mayCKzcAGnw904woXd; _ga=GA1.2.336394060.1616169129; _fbp=fb.1.1616169130230.1841616237; _xpkey=SMva9re_1Zfr49USEPm0hiW8R5Vu1cL_; _xpid=2085231525; visid_incap_774904=aQSkMHkMSy2wUZqwn2IouL5vV2AAAAAAQUIPAAAAAAAqHA5B7b9Lm7hiDnp5av0Y; ct=NL; __gads=ID=53b720b55f5792c6:T=1616784165:S=ALNI_MYEEsaYAawAOp542TaHQv1TaXNS4Q; euconsent-v2=CPFGPTzPFGPTzAKAcAENBXCsAP_AAH_AAAwIHvtf_X__b39j-_59__t0eY1f9_7_v-0zjhfdt-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQNlHOHUTUmw6okVrTPsak2Mr7NKJ7LEinMbe2dYGHtfn91TuZKYr_78_9fz__-__v___9f3r-3_3__59X---_e_V399zLv9__34HlAEmGpfABZiWODJNGlUKIEIVhIdAKACihGFomsIGVwU7K4CPUEDABAagIwIgQYgoxYBAAABAEhEQEgB4IBEARAIAAQAqQEIACJgEFgBYGAQACgGhYgRQBCBIQZHBUcpgQESLRQTyVgCUXexphCGUWAFAo_oqMBEoQQLAAAA.f_gAAAAAAAAA; addtl_consent=1~39.4.3.9.6.5.4.13.6.4.15.9.5.2.7.4.1.7.1.3.2.10.3.5.4.21.4.6.9.7.10.2.9.2.12.6.7.6.14.5.20.6.5.1.3.1.11.29.4.14.4.5.3.10.6.2.9.6.6.4.5.3.1.4.29.4.5.3.1.6.2.2.17.1.17.10.9.1.8.6.2.8.3.4.142.4.8.35.7.15.1.14.3.1.8.10.14.11.3.7.25.5.18.9.7.41.2.4.18.21.3.4.2.1.6.6.5.2.14.18.7.3.2.2.8.20.8.8.6.3.10.4.20.2.4.9.3.1.6.4.11.1.3.22.16.2.6.8.2.4.11.6.5.17.16.11.8.1.10.28.8.4.1.3.21.2.7.6.1.9.30.17.4.9.15.8.7.3.6.6.7.2.4.1.7.12.13.22.13.2.12.2.4.6.1.4.15.2.4.9.4.5.1.3.7.13.5.15.4.13.4.14.8.2.15.2.5.5.1.2.2.1.2.14.7.4.8.2.9.10.18.12.13.2.18.1.1.3.1.1.9.25.4.20.8.4.5.2.1.5.4.8.4.2.2.2.14.2.13.4.2.6.9.6.3.4.3.5.2.3.6.10.11.2.4.3.16.3.11.3.1.2.3.9.19.11.15.3.10.7.6.4.3.4.9.3.3.3.1.1.1.6.11.3.1.1.7.4.6.1.10.5.2.6.3.2.2.4.3.2.2.7.2.13.7.12.2.1.6.4.5.4.3.2.2.4.1.3.1.1.1.2.9.1.6.9.1.5.2.1.7.2.8.11.1.3.1.1.2.1.3.2.6.1.5.6.1.5.3.1.3.1.1.2.2.7.7.1.4.1.2.6.1.2.1.1.3.1.1.4.1.1.2.1.8.1.7.4.3.2.1.3.1.4.3.9.6.1.15.10.28.1.2.1.1.12.3.4.1.6.3.4.7.1.3.1.1.3.1.5.3.1.3.2.2.1.1.4.2.1.2.1.1.1.2.2.4.2.1.2.2.2.4.1.1.1.2.1.1.1.1.1.1.1.1.1.1.1.2.2.1.1.2.1.2.1.7.1.2.1.1.1.2.1.1.1.1.2.1.1.3.2.1.1.8.1.1.1.5.2.1.6.5.1.1.1.1.1.2.2.3.1.1.4.1.1.2.2.1.1.4.2.1.1.2.3.2.1.2.3.1.1.1.1.4.1.1.1.5.1.9.3.1.5.1.1.3.4.1.2.3.1.4.2.1.2.2.2.1.1.1.1.1.1.11.1.3.1.1.2.2.1.4.2.3.2.1.4.1.1.1.1.1.3.2.1.1.2.5.1.3.6.4.1.1.3.1.4.3.1.4.5.1.7.2.1.1.1.2.1.1.1.4.2.1.12.1.1.3.1.2.2.3.1.3.1.1.2.1.1.2.1.1.1.1.2.4; _pbjs_userid_consent_data=3524755945110770; _pubcid=0df9369e-c3ac-42fe-8b76-3395eace2f38; _lr_env_src_ats=false; _unifiedid=%7B%22TDID%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222021-03-23T08%3A01%3A45%22%7D; incap_ses_449_774904=au6MLjTiohcmIJ/XgCs7BuMMnGAAAAAAZINuOXpWqyZpJEdxjCJOpg==; _gid=GA1.2.1119115737.1620839653; __qca=P0-318677905-1620839654635; _lr_retry_request=true; cto_bidid=UZyIoV9kJTJGWk1oU2FFMWkzY0RnOWpEU0t1emNoUFJ0ZE9peDk2WHE5UVlwM2dwTmJDc045MzlDc1J6b0RxbDRtUmVIbFRmMzUxQzA0bUFiUnE2Z3ZqdnZZd25hc1NyMUxrWU5iM215bUZudEg0WW53JTNE; cto_bundle=X2U94F9DOWxwOFNUVWFHa2lsVUlWQjRTT2VyR3QlMkY3eHBCeWZMbFR2cHNvJTJGM09iUFY3YjdEVHNzZzduVXRxR1NDVHpubjFDUmFlNHIwSSUyQjB1NGFtN0NCQlNYUTRXYXFHNzBHZyUyQjF4czVPdVoxYkNVc1VQM2RMMndkSmJwWWhCU2dqcUMzJTJCZlBFbWRPUVglMkZSb05NeGNEJTJGZmNvQSUzRCUzRA; _gat=1; _gat_subdomainTracker=1; visid_incap_774904=xECrmCGIRmOIhlsFeHoQ+mp4W2AAAAAAQUIPAAAAAAAdiHF0B3rdX1OotNIKvQhE'
}

response = requests.request("GET", url, headers=headers, data=payload)

# this extra variables help to retrieve the CSV file
ajax=response.json()
df = pd.json_normalize(ajax['playerTableStats'])
df.to_csv('AjaxEredivisie2021.csv',index=False)

# Now I've created a CSV file named: AjaxEredvisie2021
