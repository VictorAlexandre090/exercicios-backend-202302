import requests, json, pprint
api_key = "61178d1f"
nome_do_filme = "Titanic"
base_url = "http://www.omdbapi.com/?"
#complete_url = base_url + "apikey=" + api_key + "?i=tt3896198"
complete_url = base_url + "apikey=" + api_key + "&t=" + nome_do_filme
response = requests.get(complete_url)

x = response.json()
pprint.pprint(x)
#i=tt3896198&apikey=61178d1f"
