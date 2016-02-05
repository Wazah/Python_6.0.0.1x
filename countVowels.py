s = 'cuantasvocaleshayacadecimedalechehuevon'

def numberOfVowels(s):
    number=s.lower().count('a')+s.lower().count('e')+s.lower().count('i')+s.lower().count('o')+s.lower().count('u')
    print('Number of Vowels: ' + str(number))
    
print numberOfVowels(s)