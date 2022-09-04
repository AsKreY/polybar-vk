#!/usr/bin/env python
import requests

access_token = """paste token here"""
response = requests.get("https://api.vk.com/method/account.getCounters?filter=messages&access_token={}&v=5.131"
                        .format(access_token))
if response.status_code == 200:
    msgs_json = response.json()['response']
    print(0 if len(msgs_json) == 0 else msgs_json['messages'])
else:
    print("Error: %s" % response.status_code)
