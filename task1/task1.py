import sys
import argparse as argp

def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument('--percentile', required=True)
    parser.add_argument('--mediana', required=True)
    parser.add_argument('--min', required=True)
    parser.add_argument('--max', required=True)
    parser.add_argument('--average', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

def percentile(numbers):
    percentile = int((90 * len(numbers) / 100 - 1))
    return percentile


def mediana(numbers):
    n = len(numbers)
    s = sorted(numbers)
    k = n // 2
    if n % 2 == 0:
        return 0.5 * (s[k] + s[k - 1])
    else:
        return s[k]


def min(numbers):
    min = 0
    for i in numbers:
        if (i < min):
            min = i
    return min


def max(numbers):
    max = 0
    for i in numbers:
        if (i > max):
            max = i
    return max

def average(numbers):
    s = float(sum(numbers))
    c = float(len(numbers))
    if numbers == []:
        return False
    return float(s / c)


numbers = []
with open('input.txt') as f:
    for line in f:
        numbers.append(float(line.strip()))

print(numbers)
print('%.2f' % percentile(numbers))
print('%.2f' % mediana(numbers))
print('%.2f' % min(numbers))
print('%.2f' % max(numbers))
print('%.2f' % average(numbers))




















