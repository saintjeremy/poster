# get modules requests and json then set base URL + endpoint
# giving privileges to blog via app passwords plugin
# see wordpress.org/plugins/application-passwords

import base64
import requests
import json

user = 'saintjeremy'
appcredo = 'REDACTED AND DEPRECATED'  # clever redaction
url = 'https://blisstout.com/wp-json/wp/v2'

# get token

token = base64.standard_b64encode(user + ':' + appcredo)
headers = {'Authorization': 'Basic ' + token}

# once successful interaction

post = {'date': '2018-05-09T17:10:35',
        'title': 'Poster Nut Bag',
        'slug': 'api-origin-1',
        'status': 'publish',
        'content': 'Watch out for Harpua',
        'author': '1',
        'excerpt': 'It seems to be about your cat!',
        'format': 'standard'
        }
