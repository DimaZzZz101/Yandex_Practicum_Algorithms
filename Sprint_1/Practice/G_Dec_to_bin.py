def dec_to_bin(dec):
    bin_num = ''

    while dec > 0:
        bin_num = str(dec % 2) + bin_num
        dec //= 2

    return bin_num


if __name__ == "__main__":
    dec_num = int(input())

    print(dec_to_bin(dec_num))
