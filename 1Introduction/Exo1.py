import requests


class req:
    def __init__(self) -> None:
        self.url = "http://www.esiee.fr/"
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        
        pass

    def get(self, timeout = 3, retry = 1):
        print(retry)
        if retry == 0:
            return None
        response = requests.get(self.url, headers = {'User-Agent' : self.userAgent}, timeout=timeout)
        if response.status_code == 200:
            return response
        return self.get(retry = retry - 1)

r = req()
response = r.get(timeout = 3, retry = 4)
print(response.status_code)