import requests
import random
import dynamon
import threading
import time

first_run = True

def _push(*args, id=None, path=None):
    if len(args) == 0:
        raise Exception("Missing argument.")
    elif len(args) == 1:
        if type(args[0]) is list:
            data = args[0]
        else:
            data = {
                'y': args[0]
            }
    elif len(args) == 2:
        data = {
            'x': args[0],
            'y': args[1]
        }

    if not path:
        if dynamon.path:
            path = dynamon.path
        else:
            dynamon.path = _gen_random_path()
            path = dynamon.path

    url = 'https://dynamon.io/' + path

    global first_run
    if first_run:
        print('Dynamon: ' + url)
        first_run = False

    json = {}
    json['data'] = data
    if id:
        json['id'] = id

    requests.post(url, json=json)

def _gen_random_path():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))

# Delegate the push to a separate thread, to make it non-blocking.
# TODO: Threads are inefficient. Figure out a way of doing this with asyncio.
# def push(*args, **kwargs):
#     threading.Thread(target=_push, args=args, kwargs=kwargs).start()



# This implements a cache for the requests.
# TODO: Make the cache aware of different paths and different ids.

queue = []
push_is_scheduled = False

def _push_queue():
    global push_is_scheduled
    global queue
    time.sleep(1)
    push_is_scheduled = False
    series1 = []
    for item in queue:
        series1.append({'x': item['x'], 'y': item['y']})
    data = [series1]
    kwargs = queue[0]['kwargs']
    queue = []
    threading.Thread(target=_push, args=(data,), kwargs=kwargs).start()

import datetime

def _get_now_iso():
    return datetime.datetime.utcnow().isoformat() + 'Z'

def push(*args, **kwargs):
    if len(args) == 0:
        raise Exception("Missing argument.")
    elif len(args) == 1:
        x = _get_now_iso()
        y = args[0]
    elif len(args) == 2:
        x = args[0]
        y = args[1]

    queue.append({'x': x, 'y': y, 'kwargs': kwargs})
    global push_is_scheduled
    if not push_is_scheduled:
        push_is_scheduled = True
        threading.Thread(target=_push_queue).start()
