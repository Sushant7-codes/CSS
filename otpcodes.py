# Generate all 6-digit codes using digits 0-9
import itertools

# Digits to use
digits = '0123456789'

# Generate all permutations of 6 digits
codes = [''.join(p) for p in itertools.product(digits, repeat=6)]

# Print the first few codes to verify
print("Total number of codes:", len(codes))
print("First few codes:")
for code in codes[:10]:
    print(code)

# Optionally, save all codes to a file
# with open('6_digit_codes.txt', 'w') as f:
#     for code in codes:
#         f.write(code + '\n')
