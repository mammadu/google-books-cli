import requests
import pandas

class gb:
    def __init__(self):
        self.baseurl = 'https://www.googleapis.com/books/v1/volumes?q='
        self.results_list = []

    def query_database(self, query):
        url = ''.join([self.baseurl, query])
        r = requests.get(url)
        data = r.json()
        return data

    def clear_results_list(self):
        self.results_list = []

    def update_results_list(self, results_dict):
        self.results_list.append(results_dict)

    def parse_data(self, data, length=5):
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

    def print_results_list(self):
        formatted_index = (f"{i}:" for i in range(0,len(self.results_list)))
        df = pandas.DataFrame(self.results_list, index=formatted_index)
        print(df.rename_axis('Index', axis='columns'))


    def results_of_query(self, query):
        self.clear_results_list()
        data = self.query_database(query)
        self.parse_data(data)
        self.print_results_list()

        # with open("test.json", "w") as file: #debug
        #     file.write(r.text)