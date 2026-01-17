#this is created by Foxx-etc

word = input("Enter a Word : ").lower().strip()

reg_word=[]
reg_word.extend(word)

rev_word=reg_word.copy()
rev_word.reverse()

if reg_word == rev_word:
    print("The Word Is Palindrome!")
else:
    print("The Word Is Not A Palindrome!")