import requests


class req:
    def __init__(self) -> None:
        self.url = "http://www.esiee.fr/"
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        
        pass

    def get(self, timeout = 3, retry = 1):
        if retry == 0:
            return None
        response = requests.get(self.url, headers = {'User-Agent' : self.userAgent}, timeout=timeout)
        if response.status_code == 200:
            return response
        return self.get(retry = retry - 1)

def remove_spaces(string_input):
    if string_input == "":
        return string_input
    string_fixed = string_input[0]
    for i in range(1,len(string_input)):
        if string_input[i-1] != " " or string_input[i] != " ":
            string_fixed += string_input[i]
    return string_fixed 





r = req()
response = r.get(timeout = 3, retry = 4)