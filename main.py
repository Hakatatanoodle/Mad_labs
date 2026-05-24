with open("story.txt","r") as f:
    story = f.read()



target_start = "<"
target_end = ">"
start_of_word = -1 #used to indicate that the < char has been found 

words = set() #empty set for the words 

for i,char in enumerate(story):
    if char == target_start:
        start_of_word = i #if the < char has been encountered set start_of_word to that index 
    if char == target_end and start_of_word != -1 :
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1 

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer 

for word in words: 
    story = story.replace(word,answers[word])

print(story)