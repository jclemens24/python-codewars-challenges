import array

def sale_hotdogs(n):
  if n < 5: return 100 * n
  elif n >= 5 and n < 10: return 95 * n
  else: return 90 * n

print(sale_hotdogs(10))

def sale_hotdogs_v2(n):
  return n * (100 if n < 5 else 95 if n < 10 else 90)

print(sale_hotdogs_v2(10))

def how_much_i_love_you(nb_petals):
  words = {
    1: 'I love you',
    2: 'a little',
    3: 'a lot',
    4: 'passionately',
    5: 'madly',
    0: 'not at all'
  }
  return words[nb_petals % 6]

print(how_much_i_love_you(7))

def str_count(strng, letter):
  count = 0
  for char in strng:
    if char == letter:
      count += 1
  return count

print(str_count('Hello', 'o'))
print(str_count('Hello', 'l'))

myArr = []

myArr.insert(0, { 'key': 2})
# comment
'''multi
line
comment
'''
myArr.insert(1, { 'key': 1})
def sortFunc(element):
  return element['key']
print(myArr, ',')
myArr.sort(key = sortFunc)
print(myArr)

class myPerson:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = myPerson('Jordan', 35)
print(person1.name)