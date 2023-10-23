# Fetch api data and write in to file
import requests, json, dotenv, os

dotenv.load_dotenv()


# 中央氣象局即時地震資訊
response = requests.get(f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization={os.getenv('CWB_KEY')}&format=JSON")
with open('data/cwb_earthquake.json', 'w') as f:
    json.dump(response.json(), f, ensure_ascii=False)


# Active warnings
