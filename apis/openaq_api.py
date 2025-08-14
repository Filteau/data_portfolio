'''
Some notes on OpenAQ API usage
- it uses ISO 3166 country codes
- timeframe stuff is under https://docs.openaq.org/resources/measurements
- micron stuff is under https://docs.openaq.org/resources/providers
- all data stuff is also under https://docs.openaq.org/aws/about
- API reference is under https://docs.openaq.org/api/operations
'''

import os
from openaq import OpenAQ
from dotenv import load_dotenv


# load environment vars from .env
load_dotenv()
api_key = os.getenv("OPENAQ_API_KEY")


with OpenAQ(api_key) as client:
    location = iter(client.locations.get(2178))
    client.close()

    for i in location:
        print(i)

