import requests
import pandas
import json

class gb_backend:
    def __init__(self):
        self.baseurl = 'https://www.googleapis.com/books/v1/volumes?q='
        self.results_list = []

    def query_database(self, query):
        url = ''.join([self.baseurl, query])
        response = requests.get(url)
        data = response.json()
        #debug
        # with open("bad_query.json", "w") as file:
        #     json.dump(data, file)
        # print(data) #debug
        return data

    def clear_results_list(self):
        self.results_list = []

    def update_results_list(self, results_dict):
        self.results_list.append(results_dict)

    def error_handler(self, data):
        result_dict = {
            'error code': data['error']['code']
            , "message": data['error']['message']
        }
        self.update_results_list(result_dict)

    def valid_data_handler(self, data, length):
        for i in range(length):
            result_dict = {
                'Title': data['items'][i]['volumeInfo']['title']
                , 'Authors': data['items'][i]['volumeInfo']['authors']
            }
            try:
                result_dict['Publisher'] = data['items'][i]['volumeInfo']['publisher']
            except KeyError as ex:
                result_dict['Publisher'] = 'N/A'
            self.update_results_list(result_dict)

    def parse_data(self, data, length=5):
        if list(data.keys())[0] == 'error':
            self.error_handler(data)
        else:
            if data['totalItems'] < length:
                length = data['totalItems']
            self.valid_data_handler(data, length)

    def print_results_list(self):
        formatted_index = (f"{i}:" for i in range(0,len(self.results_list)))
        dataframe = pandas.DataFrame(self.results_list, index=formatted_index)
        pandas.set_option('display.max_colwidth', None)
        print(dataframe.rename_axis('Index', axis='columns'))


    def results_of_query(self, query):
        self.clear_results_list()
        data = self.query_database(query)
        self.parse_data(data)
        self.print_results_list()
