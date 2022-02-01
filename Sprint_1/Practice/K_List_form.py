def list_form(length, form, k):
    form = int(form[:length])
    sum = " ".join(str(form + k))

    return sum


if __name__ == "__main__":
    length = int(input())
    form = input().replace(" ", "")
    k = int(input())

    print(list_form(length, form, k))
