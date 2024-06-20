
import python_weather
import asyncio
import os

async def getweather():
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
    weather = await client.get('Heilbronn')
    # returns the current day's forecast temperature (int)
    temperature = weather.temperature
    return temperature 
    


temperature = asyncio.run(getweather())
