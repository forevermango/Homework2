
   
#Raahima Ahmed
#1892523

#6.17
word = input()
password = ''
for character in word:
    if(character=='i'):
        word += '!'
    elif(character=='a'):
        word += '@'
    elif(character=='m'):
        word += 'M'
    elif(character=='B'):
        word += '8'
    elif(character=='o'):
        word += '.'
password = (word + 'qs')
#output final password
print(password)
