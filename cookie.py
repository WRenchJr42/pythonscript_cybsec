import re
import requests

def get_csrf_token(html_content):
    match = re.search(r'<meta name="csrf-token" content="([^"]+)"', html_content)
    return match.group(1) if match else None

url_first_program = "http://172.105.62.194:8000/login"
response_first_program = requests.get(url_first_program)
html_content_first_program = response_first_program.text
csrf_token = get_csrf_token(html_content_first_program)

url_second_program = "http://172.105.62.194:8000/login"
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
    'Cookie': f'laravel_session={response_first_program.cookies.get("laravel_session")}; XSRF-TOKEN={csrf_token}',
    'Upgrade-Insecure-Requests': '1'
}

payload = {
    '_token': csrf_token,
    'username': 'test1',
    'password': 'password',
    'submit': ''
}

response_second_program = requests.post(url_second_program, headers=headers, data=payload)

if response_second_program.status_code == 200:
    print("Login successful!")
    print("Cookies:", response_second_program.cookies.get_dict())
else:
    print(f"Login failed with status code {response_second_program.status_code}")
