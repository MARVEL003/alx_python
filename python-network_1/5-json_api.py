import requests
import sys


def search_user(letter):
    """POST request is sent to the given URL which contains letter param."""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        user = response.json()
        if user:
            return '[{}] {}'.format(user['id'], user['name'])
        else:
            return 'No result'
    except:
        return 'Not a valid JSON'


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ''
    print(search_user(letter))