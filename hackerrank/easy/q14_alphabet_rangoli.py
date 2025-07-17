def print_rangoli(size):
    width = 4 * size - 3
    for i in range(size):
        left = [chr(ord('a') + size - 1 - j) for j in range(i)]
        middle = chr(ord('a') + size - 1 - i)
        right = left[::-1]
        line = '-'.join(left + [middle] + right)
        print(line.center(width, '-'))
    for i in range(size - 2, -1, -1):
        left = [chr(ord('a') + size - 1 - j) for j in range(i)]
        middle = chr(ord('a') + size - 1 - i)
        right = left[::-1]
        line = '-'.join(left + [middle] + right)
        print(line.center(width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)