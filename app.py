#!/usr/bin/python3
import requests
res = requests.get("http://0.0.0.0:8000/api/kandilli/remote")

if res.status_code == 200:
    True
else:
    False
