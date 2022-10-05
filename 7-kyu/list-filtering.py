# Filter all non ints out of the list

def filter_list(l: list):
  result = []
  for val in l:
    if type(val) == int or type(val) == float:
      result.append(val)
  return result

print(filter_list([1,2,'a','b']))

# Easier to just use the "not" operator

def filter_list_v2(l: list):
  return [i for i in l if type(i) is not str]

print(filter_list_v2([1,2,'a','b']))

# Lastly, we can use isintance()

def filter_list_v3(l: list):
  return [i for i in l if isinstance(i, int)]