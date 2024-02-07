'''Write a program that reads string from user. Your program should create a dictionary
having key as word length and value is count of words of that length'''

text = input('Enter a sentence: ')
words = text.split()
d = {}
for word in words:
  if len(word) in d:
      d[len(word)] += 1
  else:
      d[len(word)]=1  
print(d)