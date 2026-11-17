# Create a text analyzer that reads a paragraph and reports word/character frequencies, longest word,
# repeated words, and basic statistics.

text = input("Enter a paragraph: ")

# Remove extra spaces and convert to lowercase
words = text.lower().split()

# 1. Basic Statistics
total_characters = len(text)
total_words = len(words)
unique_words = len(set(words))
total_spaces = text.count(" ")

print("\n--- Basic Statistics ---")
print("Total Characters:", total_characters)
print("Total Words:", total_words)
print("Unique Words:", unique_words)
print("Total Spaces:", total_spaces)

# 2. Word Frequency
word_frequency = {}

for word in words:
    word = word.strip(".,!?;:\"'()")
    if word:
        word_frequency[word] = word_frequency.get(word, 0) + 1

print("\n--- Word Frequencies ---")
for word, count in word_frequency.items():
    print(word, ":", count)

# 3. Character Frequency
character_frequency = {}

for char in text.lower():
    if char.isalpha():
        character_frequency[char] = character_frequency.get(char, 0) + 1

print("\n--- Character Frequencies ---")
for char, count in character_frequency.items():
    print(char, ":", count)

# 4. Longest Word
longest_word = ""

for word in word_frequency:
    if len(word) > len(longest_word):
        longest_word = word

print("\nLongest Word:", longest_word)

# 5. Repeated Words
print("\n--- Repeated Words ---")

found = False

for word, count in word_frequency.items():
    if count > 1:
        print(word, ":", count)
        found = True

if not found:
    print("No repeated words found!")

# 6. Average Word Length
if total_words > 0:
    average_length = sum(len(word.strip(".,!?;:\"'()")) 
                         for word in words) / total_words
    print("\nAverage Word Length:", round(average_length, 2))