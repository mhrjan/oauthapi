
import datetime

import requests
import base64

import json
import re
import logging
import urllib
import functools
import os

from hashlib import sha256

url = "https://bitbucket.org/site/oauth2/access_token"
form_data = urllib.parse.urlencode({"grant_type": "refresh_token", "refresh_token": 'Zb5h4Uuv72hyDrdJsu',"client_id": 'pZtmTWgfcMUG6TTS5V',"client_secret": 'YMeCUhjPAZzSvPKHFrLLTeWuXZjJdKyu'})
result = requests.post(url,headers={"Accept": "application/json","Content-Type": "application/x-www-form-urlencoded"},data=form_data)
print(result.json())
print(result.content)
print(result.status_code)
print(type(result))