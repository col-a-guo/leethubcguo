class WordDictionary(object):

    def __init__(self):
        self.root = {}
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        current_dictionary = self.root
        for index, letter in enumerate(word):
            if not current_dictionary.get(letter):
                current_dictionary.update({letter: {}})
            current_dictionary = current_dictionary.get(letter)
            if index == len(word)-1:
                current_dictionary.update({"end": {}})
        
    
    def base_search(self, word, dictionary):

        current_dictionary = dictionary
        if word == "" and dictionary.get("end") == {}:
            return True
        for index, letter in enumerate(word):
            if letter == ".":
                temp_list = []
                for key in current_dictionary:
                    temp_list.append(self.base_search(word[index+1:], current_dictionary.get(key)))
                return any(temp_list)
            elif not current_dictionary.get(letter):
                return False
            current_dictionary = current_dictionary.get(letter)
            if index == len(word)-1 and current_dictionary.get("end") == {}:
                return True

            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """

        return self.base_search(word, self.root)