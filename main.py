
from google import genai
import  os
key = os.environ.get('api_key')

client = genai.Client(api_key = key)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="generate stiory story for mad libs , and use <angle bracket > for placeholders , for certain words like <adjective> , <food> etc which are to be filled by the player/user the place holders should be <angle brackets > only , not () , not {} or anything  and in those  angle bracketers there is only words , no spaces in front or at the back of the angle brackets for the story , donot generate too much placeholder words neither too less , it should be of perfect length , the length suitable for a game to feel fun but not tooo long like typing a message  Dont make the story too long or too short , just the perfect length / medium Do not include anyhthin except the story , not even  Hey , here is the story  And generate different kind of stories , take multiple genres from the story books and all , make multiple settings and multiple and different characters each time"
)

story = response.text


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