#defining a function to find a given number is armstrong or not
def armstrong(n):
    copy, sum = n, 0
    while copy > 0:
        rem = copy%10
        sum += rem**(len(str(n)))
        copy//=10
    return f'{n} is an Armstrong number.' if sum == n else f'{n} is not an Armstrong number.'

if __name__ == '__main__':
    print(armstrong(153))