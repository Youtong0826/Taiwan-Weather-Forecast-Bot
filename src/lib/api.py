import json
from dotenv import load_dotenv
import requests
import os

load_dotenv()

CITYS = {
    "北部":[
        "臺北市",
        "新北市",
        "基隆市",
        "桃園市",
        "宜蘭縣",
        "新竹縣",
        "新竹市",
    ],
    "中部":[
        "苗栗縣",
        "南投縣",
        "臺中市",
        "彰化縣",
        "雲林縣",
    ],
    "南部":[
        "嘉義縣",
        "嘉義市",
        "臺南市",
        "高雄市",
        "屏東縣",
        "澎湖縣"
    ],
    "東部":[
        "臺東縣",
        "花蓮縣"
    ],
    "離島":[
        "金門縣",
        "連江縣"
    ]
}

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
    "氣象觀測":"O-A0001-001",
    "雨量觀測":"O-A0002-001",
    "即時天氣觀測":"O-A0003-001",
    "每日酸雨pH值":"O-A0004-001",
    "每日紫外線指數最大值":"O-A0005-001",
    "臭氧總觀測資料":"O-A0006-001",
    "48小時海象監測資料":"O-A0007-001",
    "":"O-A0008-001",
}

API_FORECAST_ELEMENT = {
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

    raw_data = value["records"]["locations"][0]["location"][0]["weatherElement"]
    data = [data["time"] for data in raw_data][0]

    return data

def print_element(func):
    for n in func:
        print('\"'+ n["description"] + '\":\"'+ n["elementName"] + '\",' )



#for n in get_forecast("高雄市","小港區"):
#    print('\"'+ n["description"] + '\":\"'+ n["elementName"] + '\",' )

