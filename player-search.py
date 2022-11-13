# imports
import requests
import json
import constants

# input: global vars
trackergg_key = constants.trackergg_api_key

# input: end-user input vars
print("Enter player name:")
userInput = input()

# input: request header parameters vars
platform = "origin"
platformUserIdentifier = userInput

# input: request header vars
headers = {
 "TRN-Api-Key": trackergg_key,
 "platform": platform,
 "platformUserIdentifier": platformUserIdentifier
}

# input: tracker.gg api request url vars
apex_profile = f'https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{platformUserIdentifier}'
apex_session = f'https://public-api.tracker.gg/v2/apex/standard/profile/{platform}/{platformUserIdentifier}/sessions'

# process: request data
res = requests.get(url=apex_session, params=headers)

# process: massage data
res_data = res.content.decode("utf-8")
json_data = json.loads(res_data)

# debug: show data types
### print(f'Test res content type: {type(res.content)}')
### print(f'Test res data type: {type(res_data)}')
### print(f'Test json data type: {type(json_data)}')

# output: print
print(json.dumps(json_data, indent=4))
