def is_even_factorial(n):
    if n == 0 or n == 1:
        return "NO"
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
            if factorial % 2 == 0:
                return "YES"
        return "NO"


n = int(input())
result = is_even_factorial(n)
print(result)

