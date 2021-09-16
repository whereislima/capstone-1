import requests

url = "https://sephora.p.rapidapi.com/auto-complete"

search_term = "serums"

querystring = {"q": search_term}

headers = {
    'x-rapidapi-host': "sephora.p.rapidapi.com",
    'x-rapidapi-key': "4aff8a97ccmsh04b89d869aa3d1ap1fbf25jsn746679575818"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)