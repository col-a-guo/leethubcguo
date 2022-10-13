class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 1:
            return ["()"]
        else:
            new_list = []
            old_list = self.generateParenthesis(n-1)
            for string in old_list:
                for position, char in enumerate(string):
                    new_string = "("+string[:position]+")"+string[position:]
                    if not new_string in new_list:
                        new_list.append(new_string)
            return(new_list)