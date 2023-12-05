import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import random


user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.37",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.146",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Gecko/20100101 Firefox/97.0",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "curl/7.68.0"
]

class req:
    def __init__(self,url,timeout = 3, retry = 1) -> None:
        self.url = url
        self.userAgent = user_agents[random.randint(0,len(user_agents)-1)]
        self.domain = self.get_domain()
        self.soup = self.get_soup(timeout = timeout, retry = retry)
        self.title = self.soup.head.title
        self.H1 = self.soup.find_all("h1")
        self.image_links = self.get_image_links()
        self.external_links = self.get_external_links()
        self.text = self.soup.text
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
    
    def get_soup(self, timeout = 3, retry = 1):
        response = self.get(timeout = timeout, retry = retry)
        soup = BeautifulSoup(response.text,features="lxml")
        return soup
    
    def remove_spaces(self, string_input):
        spaces = [" ","\t","\n"]
        if string_input == "":
            return string_input
        string_fixed = string_input[0]
        for i in range(1,len(string_input)):
            if not (string_input[i-1] in spaces) or not (string_input[i] in spaces):
                string_fixed += string_input[i]
        return string_fixed 

    def get_domain(self):
        parsed_url = urlparse(self.url)
        domain_name = parsed_url.netloc
        return domain_name

    def get_image_links(self):
        images = self.soup.find_all("img")
        image_links = [img['src'] for img in images]
        return image_links

    def get_external_links(self):
    
        # Find all anchor (a) elements
        anchor_elements = self.soup.find_all('a')
    
        # Extract href attributes and filter external links
        external_links = [
            urljoin(self.url, anchor.get('href')) 
            for anchor in anchor_elements 
            if anchor.get('href') and urlparse(anchor.get('href')).netloc != urlparse(self.url).netloc
        ]
    
        return external_links

    



r = req("http://www.esiee.fr/",3,1)
clean_response = r.get_clean_response(timeout = 3, retry = 4)

userAgent = r.userAgent
title = r.title
domain_name = r.domain
H1 = r.H1
image_links = r.image_links
external_links = r.external_links
text = r.text
#print(clean_response)

print(userAgent)
print(title)
print(domain_name)
print(H1)
print(image_links)
print(external_links)

