import analysis as an
import random

n2_digits = [an.leading_digit(n**2) for n in range(1,100001)]
digit_count = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
}

for digit in n2_digits:
    digit_count[digit] += 1

totalFreq = 0.0

print("Analysis of the first digit for the set {n^2 | n >= 1, n <= %d}" % (len(n2_digits)))
print('digit,\tcount,\tfreq')
print('----------------------')
for digit, count in digit_count.items():
    print("%d:\t%d,\t%.2f%%" % (digit, count, ( count / len(n2_digits) * 100 )))
    totalFreq +=  count / len(n2_digits) * 100
print('----------------------')
# print(digit_count.values())
print('total: \t%d,\t%.2f%%' % (sum(digit_count.values()), totalFreq))
