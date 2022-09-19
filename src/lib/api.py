import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_AUTHORIZATION = os.getenv("API_AUTHORZATION")

API_URL = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/"

API_FORECAST_SUFFIX = {
    "一般天氣狀況":"F-C0032-001",
    "宜蘭縣":"F-D0047-001",
    "桃園市":"F-D0047-005",
    "新竹縣":"F-D0047-009",
    "苗栗縣":"F-D0047-013",
    "彰化縣":"F-D0047-017",
    "南投縣":"F-D0047-021",
    "雲林縣":"F-D0047-025",
    "嘉義縣":"F-D0047-029",
    "屏東縣":"F-D0047-033",
    "臺東縣":"F-D0047-037",
    "花蓮縣":"F-D0047-041",
    "澎湖縣":"F-D0047-045",
    "基隆縣":"F-D0047-049",
    "新竹市":"F-D0047-053",
    "嘉義市":"F-D0047-057",
    "臺北市":"F-D0047-061",
    "高雄市":"F-D0047-065",
    "新北市":"F-D0047-069",
    "臺中市":"F-D0047-073",
    "臺南市":"F-D0047-077",
    "連江縣":"F-D0047-081",
    "金門縣":"F-C0032-085",
    "台灣":"F-C0032-089",
}

API_OBSERVATION_SUFFIX = {
    
}

API_ELEMENT = {
    "天氣預報綜合描述":"WeatherDescription",
    "12小時降雨機率":"PoP12h",
    "6小時降雨機率":"PoP6h",
    "舒適度指數":"CI",
    "天氣現象":"Wx",
    "體感溫度":"AT",
    "相對濕度":"RH",
    "露點溫度":"Td",
    "風速":"WS",
    "風向":"WD",
    "溫度":"T",
}
def get_forecast(city:str="一般天氣狀況", location:str=None, limit:int=None, element:str=None):
    headers = {"Authorization":API_AUTHORIZATION}

    params = {
        "limit":limit,
        "locationName":location,
        "elementName":element
    }

    result = requests.get(API_URL+API_FORECAST_SUFFIX[str(city)],
        headers=headers,
        params=params,
    )

    value = json.loads(result.text)

    if value["success"] != "true": return "Something went wrong"

    return value["records"]["locations"][0]["location"][0]["weatherElement"]

for n in get_wheather("高雄市","小港區"):
    print('\"'+ n["description"] + '\":\"'+ n["elementName"] + '\",' )

