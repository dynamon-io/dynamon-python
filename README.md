# Python API for [dynamon.io](https://dynamon.io)


## Installing

```
pip install dynamon
```


## Using

See [`test.py`](test.py) for an example.


## Technical details

This API caches `dynamon.push(..)` requests for `dynamon.cache_timeout` seconds
(defaulting to 1). After this time a batched http request is made with all
cached data. This is good for performance.
