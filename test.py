import re
from collections import Counter

def create_dictionary(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    common_words = [word for word, count in word_counts.items() if count > 1]
    dictionary = {word: f'({word[:4]})' for word in common_words}
    return dictionary

def compress_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        original_text = file.read()

    dictionary = create_dictionary(original_text)
    compressed_text = original_text
    for word, replacement in dictionary.items():
        compressed_text = re.sub(r'\b' + re.escape(word) + r'\b', replacement, compressed_text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(compressed_text)

    with open('dictionary.txt', 'w', encoding='utf-8') as dict_file:
        for word, replacement in dictionary.items():
            dict_file.write(f'{word}: {replacement}\n')

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    compress_text(input_file, output_file)
    print(f'Compression complete. Compressed text saved to {output_file}, dictionary saved to dictionary.txt.')
