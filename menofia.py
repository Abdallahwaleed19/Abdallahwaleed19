s = input().strip()
leftM = s.index('M')
rightF = s.rindex('F')
result = ['-'] * len(s)
result[leftM] = 'M'
result[rightF] = 'F'
for i in range(leftM + 1, rightF):
    result[i] = 'N'
print(''.join(result))
