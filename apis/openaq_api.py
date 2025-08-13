'''
Some notes on OpenAQ API usage
- it uses ISO 3166 country codes
- timeframe stuff is under https://docs.openaq.org/resources/measurements
- micron stuff is under https://docs.openaq.org/resources/providers
- all data stuff is also under https://docs.openaq.org/aws/about
- API reference is under https://docs.openaq.org/api/operations
'''


from openaq import OpenAQ

client = OpenAQ(api_key="YOUR-OPENAQ-API-KEY")
client.locations.list(parameters_id=2, limit=1000)
client.locations.list(coordinates=[136.90610, 35.14942], radius=12000, limit=1000)
client.close()


# OpenAQ example response
# url: https://api.openaq.org/v3/countries/42
#
# {
#   "meta": {
#     "name": "openaq-api",
#     "website": "/",
#     "page": 1,
#     "limit": 100,
#     "found": 1
#   },
#   "results": [
#     {
#       "id": 42,
#       "code": "KZ",
#       "name": "Kazakhstan",
#       "datetimeFirst": "2018-07-27T17:00:00Z",
#       "datetimeLast": "2024-08-31T21:07:06.731Z",
#       "parameters": [
#         {
#           "id": 1,
#           "name": "pm10",
#           "units": "µg/m³",
#           "displayName": null
#         },
#         {
#           "id": 2,
#           "name": "pm25",
#           "units": "µg/m³",
#           "displayName": null
#         },
#         {
#           "id": 19,
#           "name": "pm1",
#           "units": "µg/m³",
#           "displayName": null
#         },
#         {
#           "id": 98,
#           "name": "relativehumidity",
#           "units": "%",
#           "displayName": null
#         },
#         {
#           "id": 100,
#           "name": "temperature",
#           "units": "c",
#           "displayName": null
#         },
#         {
#           "id": 125,
#           "name": "um003",
#           "units": "particles/cm³",
#           "displayName": null
#         }
#       ]
#     }
#   ]
# }