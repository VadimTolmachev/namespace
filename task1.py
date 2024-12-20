from random import randint

list_int = []
for i in range(10):
  list_int.append(randint(1, 100))

def sum_list(list_num):
  num1 = list_num.pop()
  if len(list_int) >= 1:
    return num1 + sum_list(list_int)
  else:
      return num1

print(list_int)
print(sum_list(list_int))