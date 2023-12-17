
import urllib.error
from urllib import request as rq
from bs4 import BeautifulSoup

class funny:
    def __init__(self):
        try:
            self.url = str(input("\nEnter a URL : "))
        except Exception as x:
            print(f'ERROR : {x}')

    def game(self):
        print(f"\n Working on URL : {self.url}")
        elements = {}
        print("There are two things that are pivotal in this case:" +
              "\n 3 : The path"
              "\n 1 : The element that is searching for the the word"
              "\n 2 : The word that is getting searched"
              '\n\n You can, however, search multiple for multiple things in a webpage with this option.')
        path = input('\n\n Path (no need for placing "/" in the beginning):')
        while True:
            searching = input("\n\nEnter the searching element (Press 'q' to come out of "
                              "the loop) : ")

            if searching.lower() == 'q':
                break
            searched = input("\nEnter the word / element to be searched : ")

            elements[searching] = searched
        print(f"\n\nResulting pairs are : {elements}")
        print("\n Proceeding further...")
        url = self.url + '/' + path

        encoded_data = urllib.parse.urlencode(elements).encode('utf-8')
        read = rq.urlopen(url, data=encoded_data)
        result = read.read().decode('utf-8')
        print(result)
        html_data = result
        soup = BeautifulSoup(html_data, 'html.parser')

        lines = soup.get_text().split('\n')

        for key, value in elements.items():
            print(f"\nResults for '{key}':")
            for line in lines:
                if key in line:
                    print(line.strip())

            print(f"\nResults for '{value}':")
            for line in lines:
                if value in line:
                    print(line.strip())


if __name__ == '__main__':
    probe = funny()
    probe.game()
