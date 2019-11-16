```

# Go to the following url to get the 'code'
https://secure.meetup.com/oauth2/authorize?client_id=msc7atcbfnsuofvf8jvuiaigr8&response_type=code&redirect_uri=http://robin.com.au&scope=basic+group_edit

```

import requests
import json
from pprint import pprint

# Get from https://secure.meetup.com/meetup_api/oauth_consumers/
client_key = 'msc7atcbfnsuofvf8jvuiaigr8'
client_secret = 'so18b0i3f2mh762hfrmm28s123'
redirect_uri = 'http://robin.com.au'

code = '3682bfd4a64689263c76dfda7fb59dba' # See comment above to get the 'code'

# Get the access token

response = requests.post('https://secure.meetup.com/oauth2/access', {'code': code, 'client_id': client_key, 'client_secret': client_secret, 'grant_type': 'authorization_code', 'redirect_uri': redirect_uri})

access_token = json.loads(response.content)['access_token']

# Getting current users
#response = requests.get('https://api.meetup.com/Perth-Django-Users-Group/members?order=joined&desc=true')
# Getting pending users
response = requests.get('https://api.meetup.com/Perth-Django-Users-Group/members?status=pending&order=joined&desc=true', headers={'authorization': 'bearer ' + access_token})

many_users = json.loads(content)
some_users = many_users[0:30]

pprint(some_users, indent=4)

from pandas.io.json import json_normalize
print(json_normalize(many_members))

real_member_ids = [
    user['id']
    for user in some_users
    if user['group_profile']['answers'][0]['answer'] == '2'
]


for member_id in real_member_ids:
    # Approving one user
    response = requests.post('https://api.meetup.com/Perth-Django-Users-Group/member/approvals', {'member': member_id}, headers={'authorization': 'bearer ' + access_token})
