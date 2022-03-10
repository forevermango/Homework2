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

# #6.22
def main():
    x1 = int(input())
    y1 = int(input())
    n1 = int(input())

    x2 = int(input())
    y2 = int(input())
    n2 = int(input())

    solution_found = False

    for x in range(-10, 11):
        for y in range(-10, 11):
            if x1 * x + y1 * y == n1 and x2 * x + y2 * y == n2:
                print(x, y)
                solution_found = True

    if not solution_found:
        print("No solution")


if __name__ == '__main__':
    main()




# #7.25
def exact_change(user_total):
    dollars = user_total // 100
    user_total %= 100
    quarters = user_total // 25
    user_total %= 25
    dimes = user_total // 10
    user_total %= 10
    nickels = user_total // 5
    user_total %= 5
    pennies = user_total
    return dollars, quarters, dimes, nickels, pennies

def main():
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    else:
        if num_dollars > 1:
            print('%d dollars' % num_dollars)
        elif num_dollars == 1:
            print('%d dollar' % num_dollars)

        if num_quarters > 1:
            print('%d quarters' % num_quarters)
        elif num_quarters == 1:
            print('%d quarter' % num_quarters)

        if num_dimes > 1:
            print('%d dimes' % num_dimes)
        elif num_dimes == 1:
            print('%d dime' % num_dimes)

        if num_nickels > 1:
            print('%d nickels' % num_nickels)
        elif num_nickels == 1:
            print('%d nickel' % num_nickels)

        if num_pennies > 1:
            print('%d pennies' % num_pennies)
        elif num_pennies == 1:
            print('%d penny' % num_pennies)


if __name__ == '__main__':
    main()


# #8.10
string = input()
modified = ''.join(string.split(' '))

if(modified == modified[::-1]):
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")



#9.10
import csv

filename = input()
f = open(filename)
data = csv.reader(f, delimiter=',')
words = []
for row in data:
    for word in row:
        words.append(word.strip())

for i in range(len(words)):
    if words[i] not in words[:i]:
        count = 0
        for w in words:
            if words[i] == w:
                count += 1
        print(words[i], count)
f.close()


#HW2

#listing month values
def get_month_as_int(monthString):
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0
    return month_int

def main():
    user_string = []
    status = True
    while (status == True):
        user_string.append(input('Please enter date: '))
        if (user_string[-1] == '-1'):
            status = False

    print('\n')
    for strings in user_string:
        if (',' in strings):
            monthString = strings.split(',')[0].split()[0]
            month_int = str(get_month_as_int(monthString))
            date = strings.split(',')[0].split()[1]
            year = strings[-4:]
            final_date = month_int + '/' + date + '/' + year
            print(final_date)
        else:
            pass



main()