import multiprocessing
import requests

def get_url(url):
    try:
        return requests.get(url, timeout=2)
    except Exception as e:
        pass
        #print("Exception: %s [%s]" % (e, type(e)))

def fetch_urls_in_parallel(urls, paralellism):
    pool = multiprocessing.Pool(paralellism)
    return pool.map(get_url, urls)


def filter_ascii_only(string):
    try:
        string.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False