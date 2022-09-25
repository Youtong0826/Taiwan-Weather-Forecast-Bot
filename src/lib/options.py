from .api import CITYS,API_FORECAST_ELEMENT
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
    name="鎮市區",
    description="所要查詢的地點"
)

ELEMENT_OPTIONS_TYPE = {
    "forecast":API_FORECAST_ELEMENT
}

def element_option(type:str):
    return discord.Option(
        input_type=str,
        name="所要查詢的屬性",
        choices=ELEMENT_OPTIONS_TYPE[type].keys()
    )