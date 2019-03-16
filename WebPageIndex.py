import os
from AVLTreeMap import AVLTreeMap


class WebPageIndex:
    """WebPageIndex will contain the index representation of a web page.
    This class will help you transfer a web page (text file in this assignment) into an AVLTreeMap,
    where each key refers to each word appearing in the document, and each value represents a list
    containing the positions of this word in the file.
    Attributes:
        file_name: The name of the given web page
        avl_tree: An instance of AVLTreeMap to store the words in the given web page
        priority: The priority of the given web page which can be used in searching and ranking
    """
    def __init__(self, file_path):
        """The constructor of WebPageIndex.
        Each key refers to each word appearing in the document, and each value represents a list
        containing the positions of this word in the file.
        :param file_path: The name of the input file
        """
        self.priority = 0
        _, self.file_name = os.path.split(file_path)
        with open(file_path, "r") as file:
            data = file.read()
        data = self.remove_punctuation(data)
        data = self.lower_case(data)
        word_list = data.split()
        self.avl_tree = AVLTreeMap()
        for index, word in enumerate(word_list):
            index_list = self.avl_tree.get(word)
            if index_list is None:
                index_list = [index, ]
            else:
                index_list += [index, ]
            self.avl_tree.put(word, index_list)

    def set_priority(self, words):
        """Set the priority of this page"""
        count = self.get_count(words)
        self.priority = count

    def get_priority(self):
        """Get the priority of this page"""
        return self.priority

    def get_count(self, words):
        """
        Calculate the number of times given words appear in an article
        :param words: Some words given, separated by spaces
        :return: The number of times given words appear in the article
        """
        word_list = words.split()
        count = 0
        for word in word_list:
            index_list = self.avl_tree.get(word)
            count += 0 if index_list is None else len(index_list)
        return count

    def lower_case(self, data):
        """
        Convert all words in a given article to lowercase
        :param data: The string of given article
        :return:
        """
        return data.lower()

    def remove_punctuation(self, data):
        punc_list = [",", "(", ")", ".", "'", "\"", "[", "]", ":"]
        for punc in punc_list:
            data = data.replace(punc, " ")
        return data

    def __str__(self):
        return "<class WebPageIndex>[ filename: " + str(self.file_name) + ", priority: " + str(self.priority) + " ]"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    web_page = WebPageIndex("test data/doc1-arraylist.txt")
    web_page.set_priority("collection array in an")
    print(web_page.get_priority())
    print(web_page.get_count("github"))
