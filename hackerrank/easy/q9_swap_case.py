def swap_case(s):
    result = ''
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)