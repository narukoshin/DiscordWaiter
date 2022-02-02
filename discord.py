#!/usr/bin/env python3
import requests
import json

discord_api = {
    # test environment
    "bot_secret_token":"OTM4NTIxODcyMTQyODMxNzM3.Yfrgmw.eowY_iwHcxll8ptYQvS6kbH1INc",
    "api_uri":"https://discordapp.com/api/",
    "channel_id":"848509038093664266"
}

headers = {
    "Authorization": "Bot " + discord_api["bot_secret_token"],
    "Content-Type":"application/json"
}

body = {
    "max_age":      1800,	# integer	duration of invite in seconds before expiry, or 0 for never. between 0 and 604800 (7 days)	86400 (24 hours)
    "max_uses":     1,	    # integer	max number of uses or 0 for unlimited. between 0 and 100	0
    "temporary":    True,   # whether this invite only grants temporary membership	
    "unique":       True,   # if true, don't try to reuse a similar invite (useful for creating many unique one time use invites)	
}

if __name__ == "__main__":
    url = "%s/channels/%s/invites" % (discord_api["api_uri"], discord_api["channel_id"])
    a = requests.post(url=url, headers=headers, data=json.dumps(body))
    print(json.loads(a.text)["code"])