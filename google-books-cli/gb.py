import requests
import json

class gb:
    def __init__(self):
        self.baseurl = 'https://www.googleapis.com/books/v1/volumes?q='
        self.results_list = []

    def update_results_list(self, results_dict):
        self.results_list.append(results_dict)

    def query_database(self, query):
        url = ''.join([self.baseurl, query])
        r = requests.get(url)
        data = r.json()
        for i in range(5):
            result_dict = {
                'title': data['items'][i]['volumeInfo']['title']
                , 'authors': data['items'][i]['volumeInfo']['authors']
            }
            try:
                result_dict['publisher'] = data['items'][i]['volumeInfo']['publisher']
            except KeyError as ex:
                result_dict['publisher'] = 'N/A'
            self.update_results_list(result_dict)
            print(result_dict) #debug

        with open("test.json", "w") as file: #debug
            file.write(r.text)