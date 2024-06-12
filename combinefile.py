def combine_text(source1, source2, destination):
    combined_file = open(destination, "w")
    book1 = open(source1)
    book2 = open(source2)

    book1content = book1.read()
    book2content = book2.read()

    book1.close()
    book2.close()

    combined_content = book1content + "\n" + book2content
    combined_file.write(combined_content)
    combined_file.close()

    return combined_content

def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    return word_count

# Example usage:
file_path = './data/Dune.txt'
print(f"The number of words in the file is: {count_words_in_file(file_path)}")