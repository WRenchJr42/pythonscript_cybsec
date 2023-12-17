import requests
import re

url = 'http://testphp.vulnweb.com/search.php?test=query'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://testphp.vulnweb.com',
    'Referer': 'http://testphp.vulnweb.com/search.php?test=query',
    'Upgrade-Insecure-Requests': '1',
}

data = {
    'searchFor': 'flowers',
    'goButton': 'go',
}

response = requests.post(url, headers=headers, data=data)



if data:
    first_key = next(iter(data))
    first_value = data[first_key]
    print(f"Key: {first_key}, Value: {first_value}")

    searched_term_match = re.search(re.escape(first_value), response.text)
    if searched_term_match:
        print(f"\n\nSearched Term : {searched_term_match.group()}")
    else:
        print(f"Searched term '{first_value}' not found in the response.")
else:
    print("No data to process.")
