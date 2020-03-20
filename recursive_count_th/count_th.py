'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    countNum = 0
    if word == "":
        return 0
    def count(index, word, countNum):
        if index < len(word)-1:
            countNum = count(index+1, word, countNum)
        if word[index] == 't':
            if index == len(word) -1:
                return countNum
            if word[index+1] == 'h':
                countNum += 1
        return countNum
    
    countNum = count(0,word, countNum)
    
    return countNum

print(count_th("the"))
