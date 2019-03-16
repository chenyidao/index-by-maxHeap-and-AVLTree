from copy import copy


class WebPagePriorityQueue:
    """Use the maximum heap structure index page
    This class is based on the maximum heap implementation, and the
    most relevant web page given a particular query will have the
    highest priority value so that the page can be retrieved first
    Attributes:
        web_pages: Storage of web pages, using list
        arr: The max heap of web pages.
        curr_size: The size of max heap.
    """
    def __init__(self, web_pages, query):
        """The constructor (i.e., init ) which takes as input a query (string) and a set of WebPageIndex instances."""
        self.web_pages = web_pages
        self.arr = copy(self.web_pages)
        self.curr_size = len(self.web_pages)
        self.reheap(query)

    def peek(self):
        """Return the most relevant web page in the web page priority queue"""
        if self.curr_size <= 0:
            return None
        else:
            return self.arr[1]

    def poll(self):
        """Remove and return the most relevant web page in the web page priority queue"""
        if self.curr_size <= 0:
            return None
        max_item = self.peek()
        self.arr[1] = self.arr[self.curr_size]
        self.curr_size -= 1
        self.precolate_down(1)
        return max_item

    def reheap(self, query):
        """Takes a new query as input and reheap the web page priority queue"""
        self.arr = copy(self.web_pages)
        self.curr_size = len(self.web_pages)
        self.arr.insert(0, None)
        for i in range(1, len(self.arr)):
            self.arr[i].set_priority(query)
        self.build_heap()

    def insert(self, new_page):
        """Insert an element into the max heap"""
        self.curr_size += 1
        hole = self.curr_size
        self.arr[0] = new_page
        while new_page.get_priority() > self.arr[int(hole / 2)].get_priority():
            self.arr[hole] = self.arr[int(hole / 2)]
            hole /= 2
        self.arr[hole] = new_page

    def build_heap(self):
        for i in range(int(self.curr_size / 2), 0, -1):
            self.precolate_down(i)

    def precolate_down(self, hole):
        temp = self.arr[hole]
        while hole * 2 <= self.curr_size:
            child = hole * 2
            if child != self.curr_size and self.arr[child + 1].get_priority() > self.arr[child].get_priority():
                child += 1
            if self.arr[child].get_priority() > temp.get_priority():
                self.arr[hole] = self.arr[child]
                hole = child
            else:
                break
        self.arr[hole] = temp




