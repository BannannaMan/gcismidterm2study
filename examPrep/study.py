def fizzbuzz(max_value): 
#    for value in range(max_value):
    value = 0
    while value <= max_value:
        if value % 5 == 0 and value % 7 == 0:
            print('fizzbuzz')
        elif value % 5 == 0:
            print('fizz')
        elif value % 7 == 0:
            print('buzz')
        else:
            print(value)
        value += 1

def is_palindrome(word):
    backwards = ''
    length = len(word) * -1
    counter = -1
    while counter >= length:
        backwards += word[counter]
        counter -= 1
    if backwards == word:
        return True
    else:
        print(backwards)
        return False

def harmonic_sum(n):
    value = 1
    sumed = 0
    while value <= n:
        current_number = 1/value
        value += 1
        sumed += current_number
    return sumed

def the_raven():
    text = "Once upon a midnight dreary, while I pondered, weak and weary,\nOver many a quaint and curious volume of forgotten lore—\n\tWhile I nodded, nearly napping, suddenly there came a tapping,\nAs of some one gently rapping, rapping at my chamber door.\n\"\'Tis some visitor,\" I muttered,\"tapping at my chamber door—\n\t\tOnly this and nothing more.\""
    print(text)

def open_file(filename):
    print("Time to open the file")
    file = open(filename)
    file.close()
    print("File has been closed")

def odd_lines(filename):
    with open(filename) as file:
        output = ''
        count = 0
        for line in file:
            count +=1
            if count % 2 == 1: 
                output += line

    return output

def odd_lines2(filename):
    with open(filename) as file:
        count = 0
        for line in file:
            count += 1
    return count

def even_letters(filename):
    with open(filename) as file:
        output = ""
        for line in file:
            counter = 0
            stripped = line.strip()
            if stripped == "":
                continue
            else:
                length = len(stripped)
                while counter < length:
                    output += stripped[counter]
                    counter += 2
    return output

def average_words(filename):
    with open(filename) as file:
        for line in file:
            number = 0
            divider = 0
            stripped = line.strip()
            if stripped == "":
                continue
            else:
                tokens = stripped.split()
                number += len(tokens)
                divider += 1
    output = number / divider
    return output


def main():
#    fizzbuzz(35)
#    print(is_palindrome('penis'))
#    print(harmonic_sum(100))
#    the_raven()
#    open_file('full_grades_100.csv')
#    print(odd_lines('grades_010.csv'))
#    print(odd_lines2('alice.txt'))
#    print(even_letters("alice.txt"))
    print(average_words('alice.txt'))



if __name__ == "__main__":
    main()