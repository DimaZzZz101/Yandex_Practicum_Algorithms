def find_palindrome(phrase):
    phrase = ''.join(x for x in phrase if x.isalpha()).lower()
    reversed_phrase = ''.join(x for x in phrase[::-1] if x.isalpha()).lower()

    if phrase == reversed_phrase:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    text = input()
    print(find_palindrome(text))
