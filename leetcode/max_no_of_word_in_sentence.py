sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

def maxLenWord(sentences):
    lenght_word = 0
    for sentence in sentences:
        sentenceWord = sentence.split()
        if len(sentenceWord) > lenght_word:
            lenght_word = len(sentenceWord)
    return lenght_word

# optimeized

def maxLenWord(sentences):
    return max([len(sentence.split())for sentence in sentences])

sentences = ["please wait", "continue to fight", "continue to win"]
maxLenWord(sentences)


