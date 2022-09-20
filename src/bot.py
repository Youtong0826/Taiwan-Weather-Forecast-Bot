from dotenv import load_dotenv
from datetime import datetime
from lib.options import *
from lib.api import *
import discord
import os

load_dotenv()
INTENTS = discord.Intents.all()

bot = discord.Bot(intents=INTENTS)

@bot.command(name="天氣預報",description="查詢各地的天氣預報")
async def forecast(ctx,area:area_option,city:city_option,location:location_option):
    result = get_forecast(city,location,element="Wx")

    embed = discord.Embed(
        title=f"{city}-{location} 天氣預報",
        description=f"自{result[0]['startTime']} 至 {result[-0]['endTime']} 的報告",
        color=discord.Color.blue(),
        timestamp=datetime.utcnow()
    )

    for data in result:
        embed.add_field(
            name=f"天氣狀況: {data['elementValue'][0]['value']}",
            value=f"時間區段: {data['startTime']} ~ {data['endTime']}"
        )

    
    {
        "time": [
          {
            "startTime": "2022-09-20 18:00:00",
            "endTime": "2022-09-20 21:00:00",
            "elementValue": [
              {
                "value": "多雲",
                "measures": "自定義 Wx 文字"
              },
              {
                "value": "04",
                "measures": "自定義 Wx 單位"
              }
            ]
          },
        ]
    }

    await ctx.respond(embed=embed)

@bot.event
async def on_ready():
    print("Bot is ready!!")
    
if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))