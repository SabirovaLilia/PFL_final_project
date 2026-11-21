import os

import requests

url = 'https://github.com/ShingZhanho/verbe-conjugaison-academie-francaise/releases/download/v0.5.0/verbs.db'
filepath = 'data/verbs.db'

if not os.path.exists(filepath):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filepath, 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        print(f'Cannot download file. Error: {e}')
