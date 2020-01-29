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
repo_name = 'python_api_test'
print()
print()

# call API to get repository information
resp = requests.get('https://api.github.com/repos/' + username + '/' + repo_name + '/issues/events')
# if resp.status_code != 200:
#     # This means something went wrong
#     raise ApiError('GET /repos/' + username + '/' + repo_name + ' {}'.format(resp.status_code))

# Extract resp JSON to response variable
json_response = resp.json()
final_response = json_response[0]
# final_response = json.dumps(json_response) 
# # print(type(final_response))
# print(final_response)

# json_response = resp.json()
# final_response = json.load(json_response)
# print(type(final_response))
# print(final_response)
# Loop through each JSON object and verify if 'id' or 'name' are present
# for k, v in response.items():
#     if k == 'id':
#         print(k + ' = ' + str(v))
#     if k == 'name':
#         print(k + ' = ' + str(v))

for k, v in final_response.items():
    if k == 'id':
        print('Issues')
        print(k + ' = ' + str(v))
    if k == 'issue':
        issue = v
        print()
        print('Issue Information')
        for k, v in issue.items():
            if k == 'number':
                issue_id = v
                print('Issue ID: ' + str(issue_id))
                issue_response = requests.get('https://api.github.com/repos/' + username + '/' + repo_name + '/issues/' + str(issue_id))
                issue_response_json = issue_response.json()
                #print(issue_response_json)
                for k, v in issue_response_json.items():
                    if k == 'title':
                        print('Issue Title: ' + v)
                    if k == 'state':
                        print('Issue State: ' + v)
                    if k == 'pull_request':
                        print('Issue Pull Request: ' + str(v['url']))
                    if k == 'body':
                        print('Issue Body: ' + v)
                        


    