# Please do not modify this part of the code!
def tokenize(text):
    return text.split()


# ======== You can define the search_text function here. Do not write any code other than your solution here! ==========
def search_text(filename, query):
    content = ""
    num_of_occurences = 0
    with open(filename, 'r') as file:
        for line in file.readlines():
            content = content + line
        content = content.lower()
        content = tokenize(content)
        file.close()
    for word in content:
        if word == query:
            num_of_occurences += 1

    return num_of_occurences

# ====================================================================================================================================

if __name__ == '__main__':
	# Here you can write code to test your function. Code you write here is solely for testing and will not be evaluated.
    """
    query = 'ipsum'
    occurrences = search_text('lorem-ipsum.txt', query)

    print(f'Found {occurrences} occurrences of {query} in text.')
    """

    print(search_text('lorem-ipsum.txt', "lorem"))
