def reverse_words(s: str):
    words = s.split()
    return ' '.join(reversed(words))

# Test Cases
print(reverse_words("the sky is blue"))          # Output: "blue is sky the"
print(reverse_words("  hello world  "))          # Output: "world hello"
print(reverse_words("a good   example"))         # Output: "example good a"
print(reverse_words("    "))                     # Output: ""
print(reverse_words("word"))                     # Output: "word"
