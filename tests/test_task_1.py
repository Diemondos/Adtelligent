import requests
import json


def test_add_user():
    headers = {'Authorization': 'Token token="122b1c2f61107698e65c53e405f572a5"',
               'Content-Type': 'application/json'}
    body = json.dumps({
        "user": {
        "login": "diemond",
        "email": "diemond@gmail.com",
        "password": "123456789"
        }
    })
    response = requests.post("https://favqs.com/api/users", headers=headers, data=body)
    print(response.text)
    print(response.status_code)

def test_login_email():
    headers = {'Authorization': 'Token token="6e487e7d792ebefc08a0d3fa63a7aac4"',
               'User-Token': 'Y2wEDOOiyID6luAtxILWdvJGNDNY9I0Td0L16UeyqMlGUcZqd0K0wckHKe8QzlyqBWdsOVOdDDYYAC01/EyoIg==',
               'Content-Type': 'application/json'}
    response = requests.get('https://favqs.com//api/users/:diemond', headers=headers)
    print(response.text)
    print(response.status_code)