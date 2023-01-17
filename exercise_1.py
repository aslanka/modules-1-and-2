word = input("Enter a string: ")
word = word.replace(' ', '')
lowerString = ''
upperString = ''
for i in range(len(word)):
    if word[i].upper() == word[i]: upperString += word[i]
    else: lowerString += word[i]
print(lowerString + upperString)