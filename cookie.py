import requests
import http.cookies
import os


def get_cookies(url):
    response = requests.get(url)
    cookie_dict = {}
    for key, value in response.cookies.items():
        cookie_dict[key] = value
    return cookie_dict


def update_cookies_file(url, cookies):
    filename = "cookies_data.txt"

    try:
        with open(filename, 'r') as file:
            existing_content = file.read()
    except FileNotFoundError:
        existing_content = ""

    with open(filename, 'w') as file:
        file.write(existing_content)
        file.write(f"{url}:\n")
        for key, value in cookies.items():
            file.write(f"  {key}: {value}\n")
        file.write("\n")



if __name__ == "__main__":
    url = input("Enter URL : ")
    cookies = get_cookies(url)
    update_cookies_file(url, cookies)
    print(f"Cookies for {url} saved in cookies_data.txt")
