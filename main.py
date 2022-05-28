# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # this sorts through the letters and compares
    if (sorted(word) == sorted(anagram)):      
        ans = True
    else:
        ans = False
    print (ans)

str1 = input("Put in the first word: ")
str2 = input("Put in the second word: ")
find_anagram(str1, str2)
