def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

data="Hello i am Learning Python"
print(reverse_words(data))