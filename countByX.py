def count_by(x, n):
  return [i * x for i in range(1, n + 1)]

print(count_by(1, 10))
print(count_by(2, 5))


def count_by_v2(x, n):
  arr = [];
  for num in range(1, n + 1):
    result = num * x;
    arr.append(result)
  return arr;

print(count_by_v2(1, 10))
print(count_by_v2(2, 5))