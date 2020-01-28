# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:23:09 2020

@author: Aaron.Trafford
"""

import requests
import json

## Get username
#print('Enter your username: ')
username = 'artrafford'
print()

## Get repository name
# print('Enter the repo you would like to access: ')
repo_name = 'AAInventoryControl'
print()
print()

# call API to get repository information
resp = requests.get('https://api.github.com/repos/' + username + '/' + repo_name)
# if resp.status_code != 200:
#     # This means something went wrong
#     raise ApiError('GET /repos/' + username + '/' + repo_name + ' {}'.format(resp.status_code))

# Extract resp JSON to response variable
response = resp.json()
# Loop through each JSON object and verify if 'id' or 'name' are present
for k, v in response.items():
    if k == 'id':
        print(k + ' = ' + str(v))
    if k == 'name':
        print(k + ' = ' + str(v))
    