print '*****************'
print '**HELLO THERE!***'
print '*****************'
print '\n Welcome the the Python Palindrome Prober!\n'

def palidrome():

    print """Please enter the word you would like to check
                              for example: racecar         """

    word = raw_input(">> ")

    if word == word[::-1]:
        print 'Yes your word is a palindrome!'
    else:
        print 'Sorry this word isn\'t a palindrome :('

    print '\nHave a nice day!'

    re_play = raw_input("Want to play agian (y/n)?")

    if re_play.lower().startswith("y"):
        palidrome()
    else:
        print "Your Loss!"

palidrome()


def harder_palindrome(word):
    """ Takes in a word, and does the palindrome step by step, using a loop"""
    """ makes the [::-1] notation clearer (hopefully)"""
    for i in range(len(word)//2): #you just want to check the first half and second half
        if (word[i] == word[-i-1]): #compare last and first until you reach the middle
            pass #do nothing
        else:
            return False #oopsy, not palindrome
    return True #yay

