def find_max_length(text):
    phrase = text.split(' ')
    output_length = 0
    output_word = ""
    for word in phrase:
        if len(word) > output_length:
            output_length = len(word)
            output_word = word

    return output_word, output_length


if __name__ == "__main__":
    n = int(input())
    text = input()

    print(*find_max_length(text), sep='\n')
