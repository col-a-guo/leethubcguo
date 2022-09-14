class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        
        
                
        output = []
        sorted_strs = []
        for string in strs:
            sorted_str = sorted(string)
            checked_flag = False
            for i, check in enumerate(sorted_strs):
                if sorted_str == check:
                    checked_flag = True
                    output[i].append(string)  
        # make sure you can't get 2 of the same str
            if checked_flag == False:
                sorted_strs.append(sorted_str)
                output.append([string])
        return(output)