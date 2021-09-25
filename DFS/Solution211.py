class WordDictionary(object):

    def __init__(self):
        self.root = {}
        self.end = '#'
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w in node:
                node = node[w]
            else:
                node[w] = {}
                node = node[w]
        node[self.end] = {}
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def _search(_word, _node):
            if _word == '':
                if '#' in _node:
                    return True
                else:
                    return False
            for i, w in enumerate(_word):
                if w == '.':
                    for key in _node:
                        if _search(_word[i+1:], _node[key]):
                            return True
                    return False
                    #return any(map(_search,[_word[i + 1:] for i in range(len(_node))],[_node[_n] for _n in _node]))
                else:
                    if w in _node:
                        _node = _node[w]
                    else:
                        return False
            return self.end in _node
        node = self.root
        return _search(word, node)


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
print(obj.search("a"))

