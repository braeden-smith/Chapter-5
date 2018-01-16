#Braeden Smith
#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333

sum = 0
count = 0
average = 0

print "Enter as many numbers as you would like and I will tell you the sum, count, and average. And if you would like to quit type 'done' "

while True:
  try:
    x = input("Enter a number: ")
    if (x == "done"): 
     break
    value = float(x)
    sum = value + sum
    count = count + 1
    average = sum / count
  except:
    print("Invalid input.")
print "This is the sum:", sum
print "This is how many numbers you typed in: ", count
print "This is the average of the input: ", average