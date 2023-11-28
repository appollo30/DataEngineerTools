from socket import timeout
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re




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

    def get_clean_response(self, timeout = 3, retry = 1):
        response = self.get(timeout=timeout,retry=retry)
        html_text = response.text
        html_text_without_spaces = self.remove_spaces(html_text)
        return html_text_without_spaces

    def remove_spaces(self, string_input):
        if string_input == "":
            return string_input
        string_fixed = string_input[0]
        for i in range(1,len(string_input)):
            if not (string_input[i-1] in (" ","\t","\n")) or not (string_input[i] in (" ","\t","\n")):
                string_fixed += string_input[i]
        return string_fixed 

    def get_domain(self):
        parsed_url = urlparse(self.url)
        domain_name = parsed_url.netloc
        return domain_name



r = req()
clean_response = r.get_clean_response(timeout = 3, retry = 4)
domain_name = r.get_domain()
print(clean_response)
print(domain_name)
