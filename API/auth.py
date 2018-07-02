import requests
import json

path = "http://172.17.30.30:8888/api/v1/"

#auth
url = path + "user/auth"

headers = {
    'login': "YWRtaW4=",
    'secret': "YWRtaW4="
    }

response = requests.request("POST", url, headers=headers)

print(response.headers['Accesstoken'])
print(response.headers['Refreshtoken'])

access_token = response.headers['Accesstoken']
refresh_token = response.headers['Refreshtoken']


#refresh_token
url = path + "user/refreshToken"

headers = {
    'refreshtoken': refresh_token
    }

response = requests.request("POST", url, headers=headers)

print(response.headers['Accesstoken'])


#dashboard
url = path + "dashboard"

headers = {
    'accesstoken': access_token

    }

response = requests.request("GET", url, headers=headers)

print(response.text)


#agents_metric
url = path + "agents/metrics"

headers = {
    'accesstoken': access_token
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


#agents
url = path + "agents"

headers = {
    'accesstoken': access_token
    }

response = requests.request("GET", url, headers=headers)
res = json.loads(response.content)
agent = res[0]['Id']

print(res[0]['Id'])
print(response.json())


#agent
url = path + "agents/" + agent

headers = {
    'accesstoken': access_token
    }

response = requests.request("GET", url, headers=headers)

print(response.content)

#auth_agent
url = path + "agents/" + agent

querystring = {"auth":"true"}

headers = {
    'accesstoken': access_token
    }

response = requests.request("PATCH", url, headers=headers, params=querystring)

print(response.status_code)


#tasks_to_agent
url = path + "agents/" + agent + "/tasks"

headers = {
    'accesstoken': access_token,
    'sort': "sort_asc",
    'field': "name",
    'page': "1",
    'size': "10"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


#modules_to_agent
import requests

url = path + "agents/" + agent + "/modules"

headers = {
    'accesstoken': access_token
    }

response = requests.request("GET", url, headers=headers)

print(response.text)