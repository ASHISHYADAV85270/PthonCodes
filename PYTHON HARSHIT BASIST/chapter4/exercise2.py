def is_palindrome(word):
    if word==word[-1::-1]:
        return "yes is a palindrome"
    return "NOT A PALINDROME"

print(is_palindrome("rohan"))    
print(is_palindrome("maham"))    
print(is_palindrome("naman"))    