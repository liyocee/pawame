import requests
import json
from random import randint

GENERATOR_ENDPOINT = 'http://localhost:8000/api/v1/random/'

for i in range(100):
    random_number = randint(1, 100 + i)
    data = {
      'number': random_number
    }

    requests.post(GENERATOR_ENDPOINT, data=json.dumps(data), headers={"Content-Type":"application/json"})

