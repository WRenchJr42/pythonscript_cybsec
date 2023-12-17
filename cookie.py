import requests

url = "http://172.105.62.194:8000/login"
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
    'Cookie': 'laravel_session=eyJpdiI6ImtOV2YrSkg4T2g2NEd1UzlpTXphVmc9PSIsInZhbHVlIjoibmRROEVWSHlRaXZnY0R0ZkQvQ0JQUWExUVBGdzBDRzBUZTMvK3RETWhwaDFzbHJYcXFyb011VWhWU3JkWWl2RDgzb05SZFluNG45NTlxSDJ0SUUxQjVBM1RYazh0N2JhUWk4K2tJbFlPeTdpZ0VnRTB4S0dxK0tpc1JKalBSSEIiLCJtYWMiOiI4ZTk0MTNhNzVhMWQ1NWE2MzM3MTJiOGIxOTQ5NDUwNTcwNWZhNjE1YTIwOTM1YzZhODc2ZDJlZDgwNWZkOGExIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6IkpldSt6c3ZBL0xldTl6elpvbGs1cXc9PSIsInZhbHVlIjoiZmZXbm5tSDIwd0liZ0doRzVEZEJWbGJlREJvVFA5MHE1RE9lYys3alFLT0s2ZktqbWhtalYrUng3eHFFdGNXRnJuNEovVXo4aXhxd3pNOENBYlFLd0p3S0FBQkN1OFE5dlMxaCtiTW1RRlhUTzB6eitGSU56aE04OG83REF2ak4iLCJtYWMiOiI1NDQyY2FlNTNmMWRhOWJmNTMyOWQ5NWYxMzFjYjE0MzY5MWFhOWUzNDMyYTI1MThmY2JhNzgwNWJjN2UyMmI4IiwidGFnIjoiIn0%3D',
    'Upgrade-Insecure-Requests': '1'
}

payload = {
    '_token': 'Chwh3Mzc6JaREv6FyDJW6QToHcExdhwRs6TIrwHM',
    'username': 'test1',
    'password': 'password',
    'submit': ''
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    print("Login successful!")

    print("Cookies:", response.cookies.get_dict())


else:
    print(f"Login failed with status code {response.status_code}")

