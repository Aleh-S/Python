def reversall(text):
    if len(text) <= 1:
        return text
    return reversall(text[1:]) + text[0]

print reversall('Do I Love Milk')