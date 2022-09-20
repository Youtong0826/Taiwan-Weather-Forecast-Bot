from .api import CITYS
import discord

async def city_option_autocomplete(ctx:discord.AutocompleteContext):
    return CITYS[ctx.options["地區"]]

area_option = discord.Option(
    input_type=str,
    name="地區",
    description="所要查詢的地區",
    choices=CITYS.keys(),
)

city_option = discord.Option(
    input_type=str,
    name="城市",
    description="所要查詢的城市",
    autocomplete=city_option_autocomplete
)

location_option = discord.Option(
    input_type=str,
    name="鄉鎮市區",
    description="所要查詢的地點"
)