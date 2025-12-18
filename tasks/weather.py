import python_weather

import asyncio
import os

def weather():
    async def main() -> None:
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            city = await client.get('India')
            print(city.daily_forecasts)

    asyncio.run(main())