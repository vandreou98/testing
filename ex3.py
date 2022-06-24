import json
from datetime import datetime

import requests

counter = 0
while counter < 5:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    text = response.text
    data = json.loads(text)

    category = data["categories"]
    joke = data["value"]
    url_site = data["url"]
    if 'dev' in category:
        counter = counter + 1
        datetime_now = datetime.now()
        file_name = datetime_now.strftime("%d-%m-%Y% H:%M:%S") + ".txt"

        f = open(file_name, "w")
        f.write(f"{joke} \n{url_site} \n")
        f.close()
