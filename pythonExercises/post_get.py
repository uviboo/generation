import requests
import json

#post

url = 'https://pf-4-3-end-of-module-assessment-server.cohorte-10-js.repl.co/send_cheep'
data = {"message": "Javiera Muñoz ha spawneado en el server"}

posting = requests.post(url, json=data)

print(posting.text)

#get
response = requests.get('https://pf-4-3-end-of-module-assessment-server.cohorte-10-js.repl.co/get_cheeps?json')
trivia = json.loads(response.content)

print(trivia)
