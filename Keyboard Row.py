class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ["q","w","e","r","t","y","u","i","o","p"]
        row2 = ["a","s","d","f","g","h","j","k","l"]
        row3 = ["z","x","c","v","b","n","m"]
        ans = []
        for word in words:
            if len(word) == 1:
                ans.append(word)
            else:
                if word[0].lower() in row1:
                    for i in range(1,len(word)):
                        if word[i].lower() not in row1:
                            break
                        if word[i].lower() in row1 and i == len(word)-1:
                            ans.append(word)
                elif word[0].lower() in row2:
                    for i in range(1,len(word)):
                        if word[i].lower() not in row2:
                            break
                        if word[i].lower() in row2 and i == len(word)-1:
                            ans.append(word)
                elif word[0].lower() in row3:
                    for i in range(1,len(word)):
                        if word[i].lower() not in row3:
                            break
                        if word[i].lower() in row3 and i == len(word)-1:
                            ans.append(word)
        return ans
