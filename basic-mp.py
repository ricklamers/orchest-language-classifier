import multiprocessing
import requests


def get_url(i):
    requests.get("https://tweakers.net/")
    return i

pool = multiprocessing.Pool(5)
pool.map(get_url, range(5))