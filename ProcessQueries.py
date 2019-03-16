import os
from WebPageIndex import WebPageIndex
from WebPagePriorityQueue import WebPagePriorityQueue


class ProcessQueries:
    """This class implements a simple web search engine."""

    def __init__(self):
        self.web_pages = []
        self.queries = []

    def read(self, folder_path, queries_name):
        """Read all file from given folder
        Build a list of WebPageIndex instances from a folder containing a set of web pages.
        And also build a list of query strings
        :param folder_path: The path of folder containing the given web pages
        :param queries_name: The name of file containing query strings, e.g. "queries.txt"
        """
        files = os.scandir(folder_path)
        for file_entry in files:
            if file_entry.name == queries_name:
                with open(file_entry.path) as f:
                    self.queries = f.readlines()
            else:
                self.web_pages.append(WebPageIndex(file_entry.path))

    def query(self, query_num=None):
        """Process the user queries using the implemented WebPagePriorityQueue.
        Find the results of the query in best-to-worst order
        :return:
        """
        if len(self.queries) == 0:
            return
        else:
            max_queue = WebPagePriorityQueue(self.web_pages, self.queries[0])
            if query_num is None:
                query_num = max_queue.curr_size
            query_num = min(max_queue.curr_size, query_num)
            for query in self.queries:
                max_queue.reheap(query)
                temp = query_num
                print("Query: " + query.strip() + " [", end="")
                while temp != 0:
                    print(max_queue.poll().file_name, end=" ")
                    temp -= 1
                print("]")


if __name__ == '__main__':
    process_queries = ProcessQueries()
    # process_queries.read('C:/Users/12433/Desktop/test data/test data', "queries.txt")
    process_queries.read('test data', "queries.txt")
    process_queries.query()


