def sum_array(a):
  result = 0
  for num in a:
    result += num
  return result

print(sum_array([10, 20, 30, 40]))

def sum_array_v2(a):
  return sum(a)

print(sum_array_v2([10, 20, 30, 40]))