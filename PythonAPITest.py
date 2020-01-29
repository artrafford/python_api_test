# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 10:23:09 2020

@author: Aaron.Trafford
"""

import requests


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


# Extract resp JSON to response variable
json_response = resp.json()


for item in json_response:    
    for k, v in item.items():
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
                            pr_url = str(v['url'])
                            review_response = requests.get(pr_url + '/comments')
                            review_response_json = review_response.json()
                            print(review_response_json)
                        if k == 'created_at':
                            print('Created at: ' + v)
                        if k == 'closed_at':
                            print('Completed at: ' + v)
                        if k == 'body':
                            print('Issue Body: ' + v)
                        
                            


    