class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dict_copy = copy.deepcopy(wordDict)
        current_string = copy.deepcopy(s)
        
        
        
        for word2 in dict_copy:
            if word2 == current_string:
                return True
        
        test_bool = True
        
        while test_bool == True:
            test_bool = False
            for word1 in dict_copy:
                for word2 in dict_copy:
                    if word1 + word2 == current_string:
                        return True
                    elif word1 + word2 == current_string[0:len(word1)+len(word2)]:
                        if word1 + word2 not in dict_copy:
                            dict_copy.append(word1 + word2)
                            test_bool = True
            
        return False