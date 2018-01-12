# Exercise 2.Write another program that prompts for a series of numbers as above and 
# at the end prints out the maximum, minimum and average of the numbers.

count = 0
total = 0
avg = 0
largest = None
smallest = None
keepgoing = True
while keepgoing:
  prompt1 = 'Enter a number \n'
  line = input (prompt1)
  try:
     line = float(line)
     count = count + 1 
     total = total + line
     avg = total / count
     if smallest is None or line < smallest:
      smallest = line
     if largest is None or line > largest:
      largest = line
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print 'Invalid Input'
      continue
print "This is how many numbers you typed in:", count 
print "This is the largest number: ", largest 
print "This is the smallest number: ", smallest