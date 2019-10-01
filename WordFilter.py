import nltk
from nltk.corpus import stopwords
from nltk.corpus import nps_chat

#grabbed from nltk book
wholeChat = nps_chat.posts('10-19-20s_706posts.xml')
#chat = chat[0]


#wholeChat = [i for i in chat]

#based on geeksforgeeks code
wholeChat = [j for i in wholeChat for j in i if j not in stopwords.words("english")]


minSize = 10
wholeChat = [i for i in wholeChat if len(i) >= minSize]

chatFreqDist = nltk.FreqDist(wholeChat)

mostCommonNum = 10
commonWords = chatFreqDist.most_common(mostCommonNum)

print(commonWords)
