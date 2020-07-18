#Alice’s Adventures in Wonderland, by Lewis Carroll
import random
class Alice:
  def getTotalNumberOfWords(book):
    words = {}
    f = open(book)

    for line in f:
      w = line.lower().split()
      for word in w:
        word = word.strip(",.\"'-;!)(‘’:“”?")
        if word not in words:
          words[word] = 1
        else:
          words[word] += 1
      
    return sum(words.values())

  def getTotalUniqueWords(book):
    words = {}
    f = open(book)

    for line in f:
      w = line.lower().split()
      for word in w:
        word = word.strip(",.\"'-;!)(‘’:“”?")
        if word not in words:
          words[word] = 1
        else:
          words[word] += 1

    return len(words)

  def get20MostFrequentWords(book):
    words = {}
    f = open(book)

    for line in f:
      w = line.lower().split()
      for word in w:
        word = word.strip(",.\"'-;!)(‘’:“”?")
        if word not in words:
          words[word] = 1
        else:
          words[word] += 1

    top20 = list(words.values())
    top20.sort(reverse=True)
    top20 = top20[0:20]
    out = []
    for val in words:
      if words[val] in top20:
        out.append([val, words[val]])
    out.sort(key=lambda count: count[1],reverse=True)
    return out

  def get20MostInterestingFrequentWords(book, commonWords):
    words = {}
    f = open(book)

    for line in f:
      w = line.lower().split()
      for word in w:
        word = word.strip(",.\"'-;!)(‘’:“”?*")
        if word == "":
          continue
        if word not in words:
          words[word] = 1
        else:
          words[word] += 1

    common = {}
    num = 1
    c = open(commonWords)
    for line in c:
      line = line.strip().lower()
      if num > 100:
        break
      common[line] = 1
      num += 1
    for word in common:
      if word in words:
        del words[word]
    top20 = list(words.values())
    top20.sort(reverse=True)
    top20 = top20[0:20]
    out = []
    for val in words:
      if words[val] in top20:
        out.append([val, words[val]])
    out.sort(key=lambda count: count[1],reverse=True)
    return out

  def get20LeastFrequentWords(book):
    words = {}
    f = open(book)

    for line in f:
      w = line.lower().split()
      for word in w:
        word = word.strip(",.\"'-;!)(‘’:“”?")
        if word not in words:
          words[word] = 1
        else:
          words[word] += 1

    top20 = list(words.values())
    top20.sort()
    top20 = top20[0:20]
    out = []
    for val in words:
      if len(out) < 20:
        if words[val] in top20:
          out.append([val, words[val]])
      else:
        break
    return out

  def getFrequencyOfWord(book, findWord):
    words = {}
    f = open(book)

    count = 0
    for line in f:
      w = line.lower().split()
      for word in w:
        word = word.strip(",.\"'-;!)(‘’:“”?")
        if word == "chapter":
          count += 1
          words[count] = {}
          continue
        if word not in words[count]:
          words[count][word] = 1
        else:
          words[count][word] += 1

    counts = []
    for chapter in words:
      if findWord in words[chapter]:
        counts.append(words[chapter][findWord])
      else:
        counts.append(0)
    return counts

  def getChapterQuoteAppears(book, q):
    words = {}
    f = open(book)
    
    count = 0
    for line in f:
      if "chapter" in line.lower():
        count += 1
        words[count] = {}
        continue
      quote = line.lower().strip(",.\"'-;!)(‘’:“”?\n")
      if quote not in words[count]:
        words[count][quote] = quote
    
    for chapter in words:
      for quote in list(words[chapter].values()):
        if q in quote:
          return chapter
    return -1

  def generateSentence(book):
    output = []
    currWord = "the"
    output.append(currWord)
    for i in range(19):
      words = {}
      f = open(book)
      prevWord = ""
      for line in f:
        w = line.lower().split()
        for word in w:
          word = word.strip(",.\"'-;!)(‘’:“”?")
          if prevWord == currWord:
            if word not in words:
              words[word] = 1
            else:
              words[word] += 1
          prevWord = word
      chosen = random.sample(list(words),1)
      output.append(chosen[0])
      currWord = chosen[0]
    sentence = ""
    for word in output:
      sentence = sentence + word + " "
    sentence.strip(" ")
    return sentence

print("Total Num Words:", Alice.getTotalNumberOfWords("book.txt"))
print()
print("Total Num Unique Words:", Alice.getTotalUniqueWords("book.txt"))
print()
print("20 Most Freq Words:", Alice.get20MostFrequentWords("book.txt"))
print()
print("20 Most Interesting Words:", Alice.get20MostInterestingFrequentWords("book.txt", "commonwords.txt"))
print()
print("20 Least Freq Words:", Alice.get20LeastFrequentWords("book.txt"))
print()
print("Find word frequency:", Alice.getFrequencyOfWord("book.txt", "hatter"))
print()
print("Find quote chapter:", Alice.getChapterQuoteAppears("book.txt", "curiouser and curiouser"))
print()
print("Generate Sentence:", Alice.generateSentence("book.txt"))