"""
you need the 'sys' & 'requests' for this task
"""

import requests
import sys


url = sys.argv[1]

req = requests.get(url)
print(req.headers.get('X-Request-Id'))


# print(req.headers)  # it will show list of things available
# print(req.headers["X-Request-Id"])