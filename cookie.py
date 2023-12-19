import re
import requests
from bs4 import BeautifulSoup

def get_csrf_token(html_content):
    match = re.search(r'<meta name="csrf-token" content="([^"]+)"', html_content)
    return match.group(1) if match else None

url = "http://172.105.62.194:8000/login"
resp = requests.get(url)
content = resp.text
csrf_token = get_csrf_token(content)


headers = {
    'Host': '172.105.62.194:8000',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://172.105.62.194:8000',
    'Connection': 'close',
    'Referer': 'http://172.105.62.194:8000/login',
    'Cookie': f'laravel_session={resp.cookies.get("laravel_session")}; XSRF-TOKEN={csrf_token}',
    'Upgrade-Insecure-Requests': '1'
}

payload = {
    '_token': csrf_token,
    'username': 'test1',
    'password': 'password',
    'submit': ''
}

fire = requests.post(url, headers=headers, data=payload)

if "Welcome" in fire.text:

    print("Login successful!")
    print("Cookies:", fire.cookies.get_dict())

    soup = BeautifulSoup(fire.text, 'html.parser')
    dropdown_menu = soup.find('ul', class_='dropdown-menu scrollable-menu')
    names = [item.text.strip() for item in dropdown_menu.find_all('a')]
    print(names)
    #print(fire.text)

else:
    print(f"Login failed with status code {fire.status_code}")
