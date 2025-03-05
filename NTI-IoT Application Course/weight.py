a, b = map(int, input().split())


sum_digits_a = sum(int(i) for i in str(a))
sum_digits_b = sum(int(i) for i in str(b))


weight_a = sum_digits_a * len(str(a))
weight_b = sum_digits_b * len(str(b))


if weight_a > weight_b:
    print(1)
elif weight_b > weight_a:
    print(2)
elif weight_a == weight_b :
    print(0)
