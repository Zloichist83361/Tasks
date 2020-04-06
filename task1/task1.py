def percentile(numbers):
    percentile = float((90.0 * len(numbers) / 100.0 - 0.8))
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
with open('task1.txt') as f:
    for line in f:
        numbers.append(float(line.strip()))

print(numbers)
print(percentile(numbers))
print(mediana(numbers))
print(min(numbers))
print(max(numbers))
print(average(numbers))
