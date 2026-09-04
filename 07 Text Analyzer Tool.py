# Text Analyzer Tool

paragraph = input("Enter a paragraph: ")

vowels = 0

# String traversal for counting vowels
for i in paragraph:
    if i in "aeiouAEIOU":
        vowels = vowels + 1

# String functions
print("Words:", len(paragraph.split()))
print("Vowels:", vowels)
print("Spaces:", paragraph.count(" "))
print("Characters:", len(paragraph))