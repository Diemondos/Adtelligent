import requests
import json


def test_update_user():
    headers = {'Authorization': 'Token token="122b1c2f61107698e65c53e405f572a5"',
              'User-Token': 'Y2wEDOOiyID6luAtxILWdvJGNDNY9I0Td0L16UeyqMlGUcZqd0K0wckHKe8QzlyqBWdsOVOdDDYYAC01/EyoIg==',
              'Content-Type': 'application/json'}
    body = json.dumps({
        "user": {
        "login": "diemondo",
        "email": "dienmondo@gmail.com"
        }
    })
    response = requests.patch("https://favqs.com/api/users/diemond", headers=headers, data=body)
    print(response.text)
    print(response.status_code)

def test_login_email():
    headers = {'Authorization': 'Token token="122b1c2f61107698e65c53e405f572a5"',
               'User-Token': 'Y2wEDOOiyID6luAtxILWdvJGNDNY9I0Td0L16UeyqMlGUcZqd0K0wckHKe8QzlyqBWdsOVOdDDYYAC01/EyoIg==',
               'Content-Type': 'application/json'}
    response = requests.get('https://favqs.com//api/users/diemondo', headers=headers)
    print(response.text)
    print(response.status_code)
