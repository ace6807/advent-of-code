"""
steps

calibartion_values = ?

for each line l
  numbers = ?
  for each character c
    is c a numer?
      if yes?
        store it somewhere? -> numbers
      if no?
        ignore it

  # here we expect to have numbers populated with all the numbers in the line
  append the first and last numbers in numbers
    what if there is only 1 number?
  if length of numbers is 1 
    then append the first number to itself
  else 
    append the first and last numbers
  
  add the number to calibartion_values


add up calibartion_values
return the sum of calibartion_values
"""


calibration_values = []

for line in open('2023/day1/input.txt').read().splitlines():
    numbers = []
    for c in line:
        if c.isdigit():
            numbers.append(c)
        else:
            pass
    
    if len(numbers) == 1:
        calibration_values.append(int(numbers[0] + numbers[0]))
    else:
        calibration_values.append(int(numbers[0] + numbers[-1]))

print(sum(calibration_values))