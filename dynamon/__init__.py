import requests

def push(id, type, data):
    requests.post('http://dynamon.io', json={
        'id': id,
        'type': type,
        'data': data
    })
